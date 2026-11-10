# サンプルコード

## ARIAの操作例に使うダミーRun

`prepare_aria_demo.py` は、第4章でARIAに実験結果の比較・可視化を依頼するためのデータを用意します。学習率2通り・バッチサイズ2通り・seed2通りの組み合わせで、8件のダミーRunを作成します。モデルの学習は行わず、精度と実行時間には説明用に決めた値を使います。

リポジトリをダウンロードまたはcloneし、そのディレクトリで実行してください。

### W&Bに8件のRunを作成する

```sh
python3 -m pip install wandb
wandb login
python3 examples/prepare_aria_demo.py \
  --upload --entity YOUR-TEAM --project YOUR-PROJECT
```

`YOUR-TEAM` と `YOUR-PROJECT` を保存先に置き換えます。実行すると、そのprojectに8件のRunが追加されます。Runのconfigには、比較対象を絞り込む目印として `synthetic=True` と `dataset_version=demo-v1` が記録されます。

### ローカルでデータを確認する

```sh
python3 examples/prepare_aria_demo.py
```

W&Bへ送信せず、`examples/aria_demo_runs.csv` と `examples/aria_demo_runs.json` を生成します。この実行にはPythonの標準ライブラリだけを使います。出力先は `--out PATH` で変更できます。

## Weaveのメディア記録用サンプル

[`weave_media.py`](weave_media.py) は、第3章の記録例で使う小さなPNG画像、WAV音声、CSV、HTMLを生成します。リポジトリのルートで次を実行してください。Pythonの標準ライブラリだけを使い、外部APIへの接続は行いません。

```sh
python3 examples/weave_media.py prepare
```

出力先は `weave_media_data/` です。本文と同じ `gradient.png`、`tone.wav`、`metrics.csv`、`report.html` が作成されます。再実行すると同名ファイルを上書きします。`--data PATH` で出力先を変更できます。

任意の動画例も用意する場合は、libx264に対応したFFmpegをPATHに設定し、`--video` を追加します。

```sh
python3 examples/weave_media.py prepare --video
```

記録するコードと認証の手順は本文に掲載しています。このファイル内の `trace` サブコマンドでも同じ記録を試せます。

```sh
python3 -m pip install weave
export WANDB_PROJECT_PATH="YOUR-TEAM/YOUR-PROJECT"
# WANDB_API_KEYを環境変数に設定してから実行
python3 examples/weave_media.py trace
```

`trace` は準備したファイルを指定先のWeaveプロジェクトへ送信します。手元のファイルを本文の例で使う場合は、このスクリプトの実行は不要です。
