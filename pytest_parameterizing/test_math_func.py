import pytest
import math_func

@pytest.mark.parametrize('num1,num2,result',
                         [(7,3,10),
                          ('Hello',' world', 'Hello world'),
                          (3.5,4.5,8)])
def test_add(num1,num2,result):
    assert math_func.add(num1,num2) == result
