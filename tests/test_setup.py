"""Basic sanity check — verifies the environment is correctly installed."""


def test_python_version():
    import sys

    assert sys.version_info >= (3, 11), "Python 3.11+ required"


def test_core_imports():
    """If these imports fail, something is wrong with the installation."""
    import numpy  # noqa: F401
    import pandas  # noqa: F401
    import torch  # noqa: F401
    import pymatgen  # noqa: F401

    assert True


def test_data_folders_exist():
    import os

    required_folders = [
        "data/raw",
        "data/processed",
        "data/external",
        "src/data",
        "src/features",
        "src/models",
    ]
    for folder in required_folders:
        assert os.path.exists(folder), f"Missing folder: {folder}"
