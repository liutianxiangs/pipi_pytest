#__author__ = 'chubby_superman'
#_*_coding=utf-8 _*_
import sys
sys.path.append(r"C:\Users\Administrator\Desktop\pytest\pipi_pytest\test")
from jzcc.add import add
import pytest

def test_1(a,b):
    assert add(a,b)==10
def test_2(a,b):
    assert add(a,b)==120
if __name__ == '__main__':
    pytest.main(["-q","test_add.py"])