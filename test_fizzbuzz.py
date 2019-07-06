from fizzbuzz import *

def test_hello():
  fizzbuzz= FizzBuzz()
  assert fizzbuzz.run(1) == 1

def test_three():
  fizzbuzz= FizzBuzz()
  assert fizzbuzz.run(3) == "Fizz"

