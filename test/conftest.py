#__author__ = 'chubby_superman'
#_*_coding=utf-8 _*_


import pytest

@pytest.fixture()
def a():
    a=100
    return a

@pytest.fixture()
def b():
    b=20
    return b