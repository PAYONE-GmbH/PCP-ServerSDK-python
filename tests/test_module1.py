# tests/test_module1.py

import pytest
from pcp_serversdk_python import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0