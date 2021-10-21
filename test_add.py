from add import add
import numpy as np

import pytest 

def test_adding():
    c=add(3,5)
    assert(c==8)

def test_float():
    c=add(30.0,39.0)
    assert(np.isclose(c,69.0))

@pytest.mark.parametrize("a,b,result", [(3,5,8), (-3,4,1), (10,-3,7)])

def test_add_param(a, b, result):
    c=add(a,b)
    assert(c==result)

def test_add_error():
    with pytest.raises(TypeError):
        c=add(3,'4')
