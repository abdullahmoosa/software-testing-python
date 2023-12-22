import math_func
import pytest
import sys
def test_add():
    assert math_func.add(7,3) == 10
    assert math_func.add(7) == 9
    print("---Execution Successful---")
@pytest.mark.skipif(sys.version_info < (3,12),reason="Unsupported Python version")
@pytest.mark.number
def test_product():
    assert math_func.product(5,5) == 25
    assert math_func.product(5) == 10
@pytest.mark.strings
def test_add_strings():
    result = math_func.add('Hello ', 'world')

    assert result == 'Hello world'
    assert type(result) is str 
    assert 'Heldio' not in result
