# W&Bで始める実験管理 — 改訂第四版

CoreWeave Forge対応の第4版で使うサンプルコード・ノートブックと参照リンクを公開しています。

## サンプルノートブック

「Open in Colab」から開き、上から順に実行してください。W&Bへのログインと、保存先のteam・projectの設定は各ノートブックの冒頭にあります。

| 掲載章 | ノートブック | Colabで開く |
|---|---|---|
| 第2章 | [PyTorchによる実験管理・Artifacts・Sweeps](notebooks/experiment_tracking_pytorch.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nejumi/wandb_fun_book_public/blob/main/notebooks/experiment_tracking_pytorch.ipynb) |
| 第2章 | [画像・動画・音声・3D・分子・グラフの記録](notebooks/multimedia_logging.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nejumi/wandb_fun_book_public/blob/main/notebooks/multimedia_logging.ipynb) |
| 第2章 | [Reports APIクイックスタート](notebooks/report_api_quickstart.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nejumi/wandb_fun_book_public/blob/main/notebooks/report_api_quickstart.ipynb) |
| 第7章 | [セグメンテーション結果の分析](notebooks/segmentation_tables.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nejumi/wandb_fun_book_public/blob/main/notebooks/segmentation_tables.ipynb) |
| 第7章 | [RDKitを用いた化合物の分析](notebooks/rdkit_chemical_analysis.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nejumi/wandb_fun_book_public/blob/main/notebooks/rdkit_chemical_analysis.ipynb) |

セグメンテーションの学習には、ColabのGPUランタイムをおすすめします。マルチメディアのnuScenes追加例は、別途データを用意した場合に実行できます。

## ARIAの操作用サンプル

第4章の[比較用ダミーRunを作成するスクリプト](examples/README.md)を収録しています。ARIAの操作例を試すため、説明用の精度・実行時間を記録した8件のRunを用意します。

## 本書の参照先

- [本文・脚注のリンク集](LINKS.md)
- [リンク集のJSON版](links.json)
- [ノートブックの実行確認](verification/README.md)

[第三版のリンク集](https://github.com/nejumi/wandb_fun_book_public/tree/f53f6dd0e8aadf159e5aae1e756724ffa4bdf484)
