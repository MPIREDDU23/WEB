#!/usr/bin/env python3

def somma(a,b):
    return a + b

def test_somma() -> None:
    assert somma(1, 2) == 3
    assert somma(-1, 1) == 0
    assert somma(0, 0) == 0
    assert somma(-1, -1) == -2
    assert somma(1000000, 2000000) == 3000000
