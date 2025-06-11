import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, -1),
    (0, 0, 0),
    (-1, 1, -2),
    (100, 200, -100),
])
def test_sottrazione(a, b, expected):
    from sottrazione import sottrazione
    assert sottrazione(a, b) == expected