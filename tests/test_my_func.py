"""Test the my_module module"""
from source import add

def test_my_func():
    """Test the add function"""
    assert add(1, 2) == 3

def test_my_func_result_in_range():
    """Test the range function"""
    value = add(50, 40)
    assert 80 < value < 100
