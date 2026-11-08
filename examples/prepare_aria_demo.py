"""Create fictional run records for book examples; uploads only with --upload."""
import argparse
import csv
import json
from pathlib import Path


def build_records():
    records = []
    for learning_rate in (0.001, 0.0003):
        for batch_size in (16, 32):
            for seed in (11, 23):
                accuracy = 0.80
                accuracy += 0.04 if learning_rate == 0.0003 else 0.0
                accuracy += 0.01 if batch_size == 32 else 0.0
                accuracy += -0.004 if seed == 11 else 0.004
                records.append({
                    "run_name": f"demo-lr{learning_rate}-bs{batch_size}-s{seed}",
                    "synthetic": True,
                    "dataset_version": "demo-v1",
                    "learning_rate": learning_rate,
                    "batch_size": batch_size,
                    "seed": seed,
                    "val_accuracy": round(accuracy, 4),
                    "train_seconds": 100 if batch_size == 32 else 180,
                })
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path(__file__).parent)
    parser.add_argument("--upload", action="store_true")
    parser.add_argument("--entity")
    parser.add_argument("--project")
    args = parser.parse_args()
    if args.upload and (not args.entity or not args.project):
        parser.error("--upload requires --entity and --project")
    records = build_records()
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "aria_demo_runs.json").write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + "\n"
    )
    with (args.out / "aria_demo_runs.csv").open("w", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=records[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(records)
    print(f"Created {len(records)} fictional records in {args.out}")
    if args.upload:
        import wandb
        for row in records:
            config = {key: row[key] for key in (
                "synthetic", "dataset_version", "learning_rate", "batch_size", "seed"
            )}
            with wandb.init(
                entity=args.entity,
                project=args.project,
                name=row["run_name"],
                job_type="synthetic-demo",
                config=config,
            ) as run:
                run.log({key: row[key] for key in ("val_accuracy", "train_seconds")})
        print("Uploaded 8 synthetic runs; no model training was performed.")


if __name__ == "__main__":
    main()
