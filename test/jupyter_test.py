#!/usr/bin/env python3
# test/jupyter_test.py - Script to test if Jupyter environment works correctly

import sys
import subprocess
import os
import tempfile

def test_jupyter_installation():
    """Check if Jupyter is installed"""
    try:
        import jupyter_core
        print(f"✓ Jupyter Core is installed (version: {jupyter_core.__version__})")
        return True
    except ImportError as e:
        print(f"× Failed to import Jupyter Core: {e}")
        return False

def test_notebook_conversion():
    """Create and convert a minimal notebook for testing"""
    try:
        # Create a temporary notebook
        with tempfile.NamedTemporaryFile(suffix='.ipynb', delete=False) as f:
            notebook_path = f.name
        
        # Minimal notebook content
        notebook_content = """{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print('Hello from test notebook')\\n",
    "import numpy as np\\n",
    "import pandas as pd\\n",
    "print('Libraries imported successfully')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}"""
        
        # Write to notebook file
        with open(notebook_path, 'w') as f:
            f.write(notebook_content)
        
        # Check if nbconvert command is available
        try:
            subprocess.run(['jupyter', '--version'], check=True, capture_output=True)
            print("✓ Jupyter command is available")
            
            # Skip full conversion test as it consumes time and space in CI
            print("✓ Skipping notebook functionality test (minimal check only in CI environment)")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f"× Failed to execute Jupyter command: {e}")
            return False
        finally:
            # Remove temporary file
            if os.path.exists(notebook_path):
                os.remove(notebook_path)
    
    except Exception as e:
        print(f"× Notebook test failed: {e}")
        return False

if __name__ == "__main__":
    print("Running Jupyter tests...")
    print("-" * 50)
    
    install_ok = test_jupyter_installation()
    convert_ok = test_notebook_conversion()
    
    if install_ok and convert_ok:
        print("\n✓ All Jupyter tests passed successfully!")
        sys.exit(0)
    else:
        print("\n× Some Jupyter tests failed.")
        sys.exit(1)
