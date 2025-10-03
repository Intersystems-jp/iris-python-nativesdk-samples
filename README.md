# Native SDK for Pythonサンプル集
## 事前準備
### Git Clone

このリポジトリをGit Cloneします。

```
git clone https://github.com/Intersystems-jp/iris-python-nativesdk-samples
```

### IRIS native SDKドライバーのインストール

ドライバーは、以下のIRISインストールディレクトリ配下に存在します。

[IRISInstallDir]/dev/python

whlという拡張子を持ったファイルを探す。

IRISバージョンおよびプラットフォームによりファイル名は異なる。

以下はMacOSでの例

```python3 -m pip install --upgrade /opt/iris/dev/python/intersystems_irispython-5.1.2-cp38.cp39.cp310.cp311.cp312.cp313-cp38.cp39.cp310.cp311.cp312.cp313-macosx_10_9_universal2.whl```

### サンプル実行

#### ディレクトリ移動

```cd python```

#### irisversion.py

稼働中のIRISバージョンを表示する

(ついでにSamples.ADBK.clsのロードも行う)

```python3 irisversion.py```

#### adbk.py

Samples.ADBKというクラスのインスタンスにアクセスするサンプル

```python3 adbk.py```

#### adbk-global.py

Samples.ADBKというクラスのインスタンスにグローバルアクセスするサンプル

```python3 adbk-global.py```

#### adbk-globalnode.py

Samples.ADBKというクラスのインスタンスにグローバルアクセスするサンプル

node()を使用して繰り返し処理

```python3 adbk-globalnode.py```

#### adbk-dbapi.py

DBI-APIを使用してSQLアクセスするサンプル

```python3 adbk-dbapi.py```

#### ##
