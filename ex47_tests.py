from nose.tools import *
import ex47

def setup():
    print("setup!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!", end='')
