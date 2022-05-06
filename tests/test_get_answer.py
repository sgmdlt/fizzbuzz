import pytest
from fizzbuzz.game import get_answer

PARAMS = [
    (3, 'Fizz'),
    (5, 'Buzz'),
    (15, 'FizzBuzz'),
    (7, ''),
]


@pytest.mark.parametrize('number,answer', PARAMS)
def test_get_answer(number, answer):
    assert get_answer(number) == answer