from shiritori import *

def test_readtxt():
    assert readtxt("./tests/test1.txt") == []
    assert readtxt("./tests/test2.txt") == ["abc","defg","hijkl"]