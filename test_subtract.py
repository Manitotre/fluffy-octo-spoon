from subtract import subtract
import numpy as np

import pytest 

def test_adding():
    c=subtract(3,5)
    assert(c==-2)

def test_float():
    c=subtract(30.0,39.0)
    assert(np.isclose(c,-9.0))

@pytest.mark.parametrize("a,b,result", [(3,5,-2), (-3,4,-7), (10,-3,13)])

def test_sub_param(a, b, result):
    c=subtract(a,b)
    assert(c==result)

def test_sub_error():
    with pytest.raises(TypeError):
        c=subtract(3,'4')
