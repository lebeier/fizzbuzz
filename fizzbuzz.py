class FizzBuzz(object):
    def __init__(self):
        pass

    def run(self, num):
        if num == 3:
            return 'Fizz'
        elif num == 15:
            return 'FizzBuzz'
        elif num % 5 == 0:
            return 'Buzz'
        return num

    def run_sequence(self, max):
        return [self.run(i) for i in range(max)]
