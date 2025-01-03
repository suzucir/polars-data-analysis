# Polars Data Analysis Environment

A Docker-based development environment for data analysis using Polars, Jupyter Notebook, and Python 3.9.

## Prerequisites

- Docker installed on your system
- Git (optional, for cloning the repository)

## Quick Start

1. Build the Docker image:
bash
./01-docker_build.sh
or
docker build -t polars-data-analysis .


2. Run the container:
bash
./02-docker_run.sh
or
docker run -p 8888:8888 -v ${PWD}:/app polars-data-analysis


3. Open your web browser and navigate to the URL shown in the terminal output (usually starts with `http://127.0.0.1:8888/...`)

## Installed Packages

- Polars
- NumPy
- Pandas
- Matplotlib
- Seaborn
- scikit-learn
- Jupyter

## Features

- Python 3.9 base environment
- Jupyter Notebook server accessible via browser
- Volume mounting for persistent notebook storage
- Pre-installed data science packages
- Polars for high-performance data manipulation

## Development

The project uses volume mounting (`-v ${PWD}:/app`) to sync the local directory with the container's `/app` directory. Any changes made to notebooks or other files will persist on your local machine.

## License

This project is open-source and available under the MIT License.
