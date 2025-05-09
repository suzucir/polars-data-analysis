FROM python:3.11-slim

LABEL maintainer="Your Name <your.email@example.com>"
LABEL description="Data Science and ML Development Environment"

# 環境変数の設定
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    DEBIAN_FRONTEND=noninteractive

# 作業ディレクトリを設定
WORKDIR /app

# システムパッケージのインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    git \
    curl \
    libopenblas-dev \
    liblapack-dev \
    libjpeg-dev \
    libpng-dev \
    wget \
    ffmpeg libsm6 libxext6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# requirements.txtをコピーしてパッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# プロジェクトファイルをコンテナにコピー
COPY . .

# Jupyter関連の設定
EXPOSE 8888

# コンテナ起動時に実行するコマンド
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token='yourtoken'"]
