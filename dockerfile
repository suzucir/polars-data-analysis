# ベースイメージを指定する(例ではPython 3.9の公式イメージを使用)
FROM python:3.11

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    git \
    curl \
    libopenblas-dev \
    liblapack-dev \
    libjpeg-dev \
    libpng-dev \
    wget \
    software-properties-common \
    ffmpeg libsm6 libxext6 \  # OpenCVの依存関係
    && rm -rf /var/lib/apt/lists/*

# プロジェクトファイルをコンテナにコピー
COPY . /app

# 必要なPythonパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# Jupyter Notebookの設定
EXPOSE 8888

# コンテナ起動時に実行するコマンド
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
