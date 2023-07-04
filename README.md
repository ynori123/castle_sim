# 城の防衛シミュレーションツール
## 概要
お城の通路をイメージして作成したシミュレーションツールです。攻撃者はスタート地点からゴール地点まで一定の速度で移動し、防衛者は防衛地点から一定の間隔で火縄銃を撃ちます。火縄銃で撃たれた弾丸は、距離に応じた確率で攻撃者に命中し、弾丸が命中した攻撃者は死亡します。

## 環境構築
1. まず、Python3の環境を構築してください。
1. このレポジトリをローカルにクローンし、クローンしたディレクトリにChange Directory(cd)してください。
1. 次に、必要なライブラリをインストールしてください。次のコマンドでインストールできます。

    Mac(bash/zsh)
    ```zsh
    $ pip3 install -r requirements.txt
    ```

    Windows
    ```shell
    > pip install -r requirements.txt
    ```
## シミュレーション方法
` sim.py `ファイルにて、攻撃者の速さ（秒速）、攻撃者の人数（整数）、防衛者が火縄銃を一発撃つのにかかる時間（秒）、スタート地点、ゴール地点の座標（タプル）を設定できます。

` control.py `ファイルにて、何回シミュレーションするかを設定できます。主に、このファイルを実行することによって` sim.py `が実行され、シミュレーションされます。シミュレーションした回数の平均値・平均通過率が出力されます。

` spot.csv `ファイルにて、防衛地点の座標、個数とその防衛地点の人数（同時に銃撃できる回数）を設定できます。` x座標,y座標,人数 `のフォーマットで編集してください。


※座標の単位はメートルを想定して命中率を計算しています。