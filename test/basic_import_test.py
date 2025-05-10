#!/usr/bin/env python3
# test/basic_import_test.py - Script to test package imports and basic functionality

import sys
import importlib

def test_imports():
    """Test imports of key packages"""
    required_packages = [
        'numpy', 
        'pandas', 
        'matplotlib', 
        'sklearn', 
        'polars', 
        'jupyter'
    ]
    
    failed_imports = []
    successful_imports = []
    
    for package in required_packages:
        try:
            module = importlib.import_module(package)
            if hasattr(module, '__version__'):
                successful_imports.append(f'{package} ({module.__version__})')
            else:
                successful_imports.append(package)
        except ImportError as e:
            failed_imports.append(f'{package}: {str(e)}')
    
    # Display results
    if failed_imports:
        print("Failed imports:")
        for failure in failed_imports:
            print(f"  × {failure}")
        return False
    else:
        print("All packages imported successfully:")
        for success in successful_imports:
            print(f"  ✓ {success}")
        return True

def test_basic_functionality():
    """Test basic data processing functionality"""
    try:
        # Import necessary libraries
        import numpy as np
        import pandas as pd
        import polars as pl
        import matplotlib.pyplot as plt
        from sklearn.datasets import make_classification
        
        print("\nTesting basic functionality:")
        
        # Basic NumPy operations
        arr = np.array([1, 2, 3, 4, 5])
        np_result = arr.mean()
        print(f"  ✓ NumPy array created and computed mean: {np_result}")
        
        # Basic Pandas operations
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        pd_result = df.mean().mean()
        print(f"  ✓ Pandas DataFrame created and computed mean: {pd_result}")
        
        # Basic Polars operations
        pldf = pl.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        pl_result = pldf.mean().to_series().mean()
        print(f"  ✓ Polars DataFrame created and computed mean: {pl_result}")
        
        # Basic scikit-learn operations
        X, y = make_classification(n_samples=10, n_features=4, random_state=42)
        print(f"  ✓ Created scikit-learn dataset with shape: {X.shape}")
        
        return True
    except Exception as e:
        print(f"Basic functionality test failed: {e}")
        return False

if __name__ == "__main__":
    print(f"Python version: {sys.version}")
    print("-" * 50)
    
    imports_ok = test_imports()
    functionality_ok = test_basic_functionality()
    
    if imports_ok and functionality_ok:
        print("\n✓ All tests passed successfully!")
        sys.exit(0)
    else:
        print("\n× Some tests failed.")
        sys.exit(1)
