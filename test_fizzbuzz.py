from fizzbuzz import *


def test_should_return_one():
    fizzbuzz = FizzBuzz()
    assert fizzbuzz.run(1) == 1


def test_should_return_two():
    fizzbuzz = FizzBuzz()
    assert fizzbuzz.run(2) == 2


def test_should_return_Fizz():
    fizzbuzz = FizzBuzz()
    assert fizzbuzz.run(3) == "Fizz"


def test_should_return_Buzz():
    fizzbuzz = FizzBuzz()
    assert fizzbuzz.run(5) == "Buzz"


def test_should_return_FizzBuzz():
    fizzbuzz = FizzBuzz()
    assert fizzbuzz.run(15) == "FizzBuzz"


def test_should_return_10_Buzz():
    fizzbuzz = FizzBuzz()
    assert fizzbuzz.run_sequence(10) == ['FizzBuzz', 1, 2, 'Fizz', 4, "Buzz", 6, 7, 8, 9]
