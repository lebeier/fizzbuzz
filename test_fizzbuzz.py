from fizzbuzz import *

def test_should_return_one():
  fizzbuzz= FizzBuzz()
  assert fizzbuzz.run(1) == 1

def test_should_return_two():
  fizzbuzz= FizzBuzz()
  assert fizzbuzz.run(2) == 2

def test_should_return_Fizz():
  fizzbuzz= FizzBuzz()
  assert fizzbuzz.run(3) == "Fizz"

def test_should_return_Buzz():
  fizzbuzz= FizzBuzz()
  assert fizzbuzz.run(5) == "Buzz"

def test_should_return_FizzBuzz():
  fizzbuzz= FizzBuzz()
  assert fizzbuzz.run(15) == "FizzBuzz"

def test_should_return_10_Buzz():
  fizzbuzz = FizzBuzz()
  for i in range(10):
    assert fizzbuzz.run(i*5) == "Buzz"

