class FizzBuzz(object):
  def __init__(self):
    pass

  def run(self, num):
    if num == 3:
      return 'Fizz'
    elif num == 5:
      return 'Buzz'
    elif num == 15:
      return 'FizzBuzz'
    return num
