# ARIAの操作例に使うダミーRun

`prepare_aria_demo.py` は、第4章でARIAに実験結果の比較・可視化を依頼するためのデータを用意します。学習率2通り・バッチサイズ2通り・seed2通りの組み合わせで、8件のダミーRunを作成します。モデルの学習は行わず、精度と実行時間には説明用に決めた値を使います。

リポジトリをダウンロードまたはcloneし、そのディレクトリで実行してください。

## W&Bに8件のRunを作成する

```sh
python3 -m pip install wandb
wandb login
python3 examples/prepare_aria_demo.py \
  --upload --entity YOUR-TEAM --project YOUR-PROJECT
```

`YOUR-TEAM` と `YOUR-PROJECT` を保存先に置き換えます。実行すると、そのprojectに8件のRunが追加されます。Runのconfigには、比較対象を絞り込む目印として `synthetic=True` と `dataset_version=demo-v1` が記録されます。

## ローカルでデータを確認する

```sh
python3 examples/prepare_aria_demo.py
```

W&Bへ送信せず、`examples/aria_demo_runs.csv` と `examples/aria_demo_runs.json` を生成します。この実行にはPythonの標準ライブラリだけを使います。出力先は `--out PATH` で変更できます。
