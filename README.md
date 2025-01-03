# Polars Data Analysis Docker Environment

This project provides a Docker environment for data analysis using Python and Polars, a lightning-fast DataFrame library.

## Features

- Ready-to-use Docker environment for data analysis
- Python with Polars DataFrame library pre-installed
- Jupyter Notebook/Lab support
- Volume mapping for persistent data storage

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/yourusername/polars-data-analysis.git

2. Navigate to the project directory:
```bash
cd polars-data-analysis

## Project Structure


## Usage

1. Access Jupyter Lab at `http://localhost:8888`
2. Your work will be saved in the `notebooks` directory
3. Place your data files in the `data` directory

## Environment Details

- Python 3.x
- Polars
- Jupyter Lab
- Common data science packages

## Stopping the Environment

To stop the Docker container:
```bash
docker-compose down
