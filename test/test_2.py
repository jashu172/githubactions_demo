# test_2.py
import os, sys
sys.path.insert(0, os.getcwd())
from scripts import addition
def test_data_type():
    subj = addition(2, 3)
    assert isinstance(subj, int)