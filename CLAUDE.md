# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Architecture Overview

This is a Docker-based data analysis environment focused on Polars for high-performance data manipulation. The project uses containerization to provide a consistent development environment with Jupyter Lab and pre-installed data science libraries.

**Core Components:**
- Main Docker environment with Python 3.11 and full data science stack
- Lightweight CI Docker image for automated testing
- Volume-mounted development workflow for persistent storage
- Automated GitHub Actions CI/CD pipeline

## Common Commands

### Build and Run
```bash
# Build the main Docker image
./01-docker_build.sh
# or directly: docker build -t polars-data-analysis .

# Run the container with Jupyter Lab
./02-docker_run.sh
# or directly: docker run -p 8888:8888 -v ${PWD}:/app polars-data-analysis

# Run with custom host directory
./02-docker_run.sh -d /path/to/your/data
```

### Testing
```bash
# CI tests are automatically run on push/PR
# To run tests locally, execute them inside the container:
python test/basic_import_test.py
python test/jupyter_test.py
```

### Access
- Jupyter Lab: http://127.0.0.1:8888/
- Default token: `yourtoken`

## Development Workflow

1. Build the Docker image using the build script
2. Run the container which starts Jupyter Lab server
3. Access Jupyter Lab in browser with the provided token
4. Work with notebooks in the mounted volume (changes persist locally)
5. CI automatically validates environment on code changes

## Dependencies

**Main Environment** (`requirements.txt`):
- Core: numpy, pandas, polars, matplotlib, seaborn, plotly
- ML: scikit-learn, xgboost, alphapy
- Tools: jupyter, jupyterlab, streamlit, dash
- Many ML/DL packages are commented out for lighter builds

**CI Environment** (`requirements-ci.txt`):
- Minimal subset for faster CI builds
- Includes essential packages: numpy, pandas, polars, scikit-learn, jupyter-core, pytest

## Docker Configuration

**Main Dockerfile** (`dockerfile`):
- Base: python:3.11-slim
- Includes system dependencies for numerical computing
- Exposes port 8888 for Jupyter Lab
- Working directory: `/app`

**CI Dockerfile** (`Dockerfile.ci`):
- Lightweight version for testing
- Uses ci-specific requirements
- Built dynamically during CI process

## CI/CD Pipeline

GitHub Actions workflow triggers on:
- Push to main/master/develop branches
- Pull requests to main/master
- Changes to Dockerfile, requirements.txt, test files, or workflow files

CI process includes disk cleanup, dynamic CI image creation, import testing, and artifact generation.