import argparse
import io
import math
from pathlib import Path
import shutil
import struct
import subprocess
import wave
import zlib


def png_bytes():
    width, height = 64, 64
    rows = b"".join(b"\x00" + b"".join(bytes((x * 4, y * 4, 128))
                                      for x in range(width))
                    for y in range(height))
    def chunk(kind, data):
        return (struct.pack(">I", len(data)) + kind + data
                + struct.pack(">I", zlib.crc32(kind + data) & 0xffffffff))
    return (b"\x89PNG\r\n\x1a\n"
            + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(rows)) + chunk(b"IEND", b""))


def wav_bytes():
    buffer = io.BytesIO()
    rate = 16000
    samples = b"".join(struct.pack("<h", int(4000 * math.sin(2 * math.pi * 440 * t / rate)))
                       for t in range(rate))
    with wave.open(buffer, "wb") as audio:
        audio.setnchannels(1)
        audio.setsampwidth(2)
        audio.setframerate(rate)
        audio.writeframes(samples)
    return buffer.getvalue()


def prepare(folder, video):
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "gradient.png").write_bytes(png_bytes())
    (folder / "tone.wav").write_bytes(wav_bytes())
    (folder / "metrics.csv").write_text("step,loss\n0,0.8\n1,0.4\n", encoding="utf-8")
    (folder / "report.html").write_text(
        "<!doctype html><html><meta charset='utf-8'><title>Weave fixture</title>"
        "<body><h1>教材データ</h1><p>モデルの生成結果ではありません。</p></body></html>",
        encoding="utf-8")
    if video:
        ffmpeg = shutil.which("ffmpeg")
        if ffmpeg is None:
            raise RuntimeError("--video requires ffmpeg on PATH")
        subprocess.run([ffmpeg, "-hide_banner", "-loglevel", "error", "-y",
                        "-f", "lavfi", "-i", "color=c=blue:s=64x64:r=10:d=1",
                        "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p",
                        str(folder / "blue.mp4")], check=True, timeout=60)


def trace(folder):
    import os
    from typing import Annotated, Literal
    import weave
    from weave import Content

    weave.init(os.environ["WANDB_PROJECT_PATH"])

    @weave.op()
    def load_image(path: str) -> Annotated[bytes, Content[Literal["png"]]]:
        return Path(path).read_bytes()

    @weave.op()
    def load_audio(path: str) -> Annotated[bytes, Content[Literal["wav"]]]:
        return Path(path).read_bytes()

    @weave.op()
    def load_document(path: str) -> Content:
        return Content.from_path(path)

    @weave.op()
    def load_video(path: str) -> Annotated[bytes, Content[Literal["mp4"]]]:
        return Path(path).read_bytes()

    load_image(str(folder / "gradient.png"))
    load_audio(str(folder / "tone.wav"))
    load_document(str(folder / "metrics.csv"))
    load_document(str(folder / "report.html"))
    if (folder / "blue.mp4").exists():
        load_video(str(folder / "blue.mp4"))
    print("教材ファイルの記録処理を実行しました。Tracesで各Callを確認してください。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["prepare", "trace"])
    parser.add_argument("--data", type=Path, default=Path("weave_media_data"))
    parser.add_argument("--video", action="store_true")
    args = parser.parse_args()
    if args.mode == "prepare":
        prepare(args.data, args.video)
    else:
        trace(args.data)
