# problem1.py
#
# ICS 32A Fall 2023
# Exercise Set 1
#
# This script asks users to specify their name and age, then,
# afterward, says "hello" to them and acknowledges how old
# they are.


def run() -> None:
    name = read_name()
    age = read_age()
    say_hello(name, age)

run()

def say_hello(name: str, age: int) -> None:
    print(f'Hello, {name}.')
    print(f"So, I hear you're {age} {pluralize('year', 'years', age)} old.")


def pluralize(singular_word: str, plural_word: str, n: int) -> str:
    if n != 1:
        return plural_word
    else:
        return singular_word


def read_name() -> str:
    return input('Enter your name: ')


def read_age() -> int:
    return int(input('Enter your age: '))

