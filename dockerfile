# ベースイメージを指定する(例ではPython 3.9の公式イメージを使用)
FROM python:3.11

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# プロジェクトファイルをコンテナにコピー
COPY . /app

# 必要なPythonパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# Jupyter Notebookの設定
EXPOSE 8888

# コンテナ起動時に実行するコマンド
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]
