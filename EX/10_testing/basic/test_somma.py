#!/opt/homebrew/bin/python3

import pytest
from somma import somma

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_somma(a, b, expected):
    assert somma(a, b) == expected
