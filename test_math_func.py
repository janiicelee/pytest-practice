import math_func
import pytest
import sys

@pytest.mark.skipif(sys.version_info < (3, 3), reason = "do not test")
def test_add():
    assert math_func.add(7, 3) == 10 
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7
    print(math_func.add(7,3), '------------------')


def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10 #꼭 같지 않아도됨.다른 부호사용


def test_add_strings():
    result = math_func.add('Hello ', 'World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Heldo' not in result 


def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result
