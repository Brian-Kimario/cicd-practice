import sys
import os

# Dynamically add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from math_utils import add, divide, multiply  # Now Python is forced to see it!

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_multiply():
    assert multiply(3, 4) == 12
