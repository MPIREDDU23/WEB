#!/usr/bin/env python3

def sottrazione(a, b):
    return a - b

def test_sottrazione() -> None:
    assert sottrazione(1, 2) == -1
    assert sottrazione(-1, 1) == -2
    assert sottrazione(0, 0) == 0
    assert sottrazione(-1, -1) == 0
    assert sottrazione(1000000, 2000000) == -1000000