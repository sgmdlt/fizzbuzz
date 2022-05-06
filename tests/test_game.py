import pytest
from fizzbuzz.game import game
from fizzbuzz.greeting import greeting
from tests.utils import FakePrompt, FakeOut

PARAMS = [(
    [15, 5, 3, 8],
    ['FizzBuzz!', 'Buzz!', 'Fizz!', 'Maybe try another one!'],
)]


@pytest.mark.parametrize('numbers, answers', PARAMS)
def test_game(numbers, answers):
    prompt = FakePrompt(numbers)
    out = FakeOut()
    answers.insert(0, greeting())
    
    game(
        from_input=prompt.get_number,
        to_output=out.write,
        end=len(prompt.numbers)
    )

    assert out.storage == answers