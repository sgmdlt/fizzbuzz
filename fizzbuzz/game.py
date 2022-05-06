import prompt
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


def game(input, output):
    print(greeting())
    while True:  # noqa: WPS457
        number = prompt.integer('Number: ')
        answer = get_answer(number)
        if answer:
            print('{0}!'.format(answer))
        else:
            print('Maybe try another one!')