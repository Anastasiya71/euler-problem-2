import pytest
from main import fib


@pytest.mark.parametrize("test_input,expected", [(6, 13), (1, 1), (-55, 1),
                                                 (0, 1)])
def test_fib(test_input, expected):
    assert fib(test_input) == expected
