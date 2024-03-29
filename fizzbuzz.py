class FizzBuzz(object):
    def __init__(self):
        pass

    def _is_fizz(self, num):
        return num % 3 == 0 or str(3) in str(num)

    def _is_buzz(self, num):
        return num % 5 == 0 or str(5) in str(num)

    def run(self, num):
        result = ''
        if self._is_fizz(num):
            result += 'Fizz'
        if self._is_buzz(num):
            result += 'Buzz'

        if result:
            return result
        return num

    def run_sequence(self, max):
        return [self.run(i) for i in range(max)]
