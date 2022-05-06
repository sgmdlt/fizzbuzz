from itertools import count
from fizzbuzz.greeting import greeting

RULES = {  # noqa: WPS407
    3: 'Fizz',
    5: 'Buzz',
}


def _multiply_of(n, m):
    return n % m == 0


def get_answer(num):
    answer = ''
    for divider in sorted(RULES):
        if _multiply_of(num, divider):
            answer += RULES[divider]
            num //= divider
    return answer


MESSAGES = {
    'prompt': 'Number: ',
    'correct_answer': '{answer}!'.format,
    'incorrect_answer': 'Maybe try another one!',
}

def game(from_input, to_output, end):
    to_output(greeting())

    for turn in count(1):
        number = from_input(MESSAGES['prompt'])
        answer = get_answer(number)
        if answer:
            to_output(MESSAGES['correct_answer'](answer=answer))
        else:
            to_output(MESSAGES['incorrect_answer'])
        if end and turn == end:
            break