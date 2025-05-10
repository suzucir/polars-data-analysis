#!/bin/zsh
# 初期値として現在のディレクトリを設定
HOST_DIR=${PWD}

# オプション解析
while getopts "d:" opt; do
  case $opt in
    d)
      HOST_DIR=$OPTARG
      # 指定されたディレクトリが存在するか確認
      if [ ! -d "$HOST_DIR" ]; then
        echo "エラー: 指定されたディレクトリ '$HOST_DIR' は存在しません"
        exit 1
      fi
      ;;
    \?)
      echo "使用法: $0 [-d ホストディレクトリのパス]"
      exit 1
      ;;
  esac
done

echo "マウントするホストディレクトリ: $HOST_DIR"
docker run -p 8888:8888 -v ${HOST_DIR}:/app polars-data-analysis