import unittest


class FizzBuzz:
    def say(self, number):
        if number % 3 == 0 and number % 5 == 0:
            return 'FizzBuzz'
        elif number % 3 == 0:
            return 'Fizz'
        elif number % 5 == 0:
            return 'Buzz'
        else:
            return number
        

class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.f = FizzBuzz()
        
    def test_input_is_divisible_by_3_should_get_fizz(self):
        self.assertEqual(self.f.say(3), 'Fizz')
        self.assertEqual(self.f.say(6), 'Fizz')
        
    def test_input_is_divisible_by_5_should_get_buzz(self):
        self.assertEqual(self.f.say(5), 'Buzz')
        self.assertEqual(self.f.say(10), 'Buzz')

    def test_input_is_divisible_by_3_and_5_should_get_fizzbuzz(self):
        self.assertEqual(self.f.say(15), 'FizzBuzz')
        self.assertEqual(self.f.say(30), 'FizzBuzz')

    def test_input_is_number_should_get_number(self):
        self.assertEqual(self.f.say(2), 2)
        self.assertEqual(self.f.say(7), 7)

    
if __name__ == '__main__':
    unittest.main()