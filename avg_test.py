from mathmodule_pkg import *

def test_am():
    assert am([1, 2]) == fraction(3, 2)

def test_gm():
    assert gm([1, 2]) == 2**(1/2)

def test_hm():
    assert hm([1, 2]) == 4/3

def test_median():
    assert median([1, 2, 3]) == 2