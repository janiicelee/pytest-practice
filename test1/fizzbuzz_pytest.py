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


def test_input_is_divisible_by_3_should_get_fizz():
    f = FizzBuzz()
    assert f.say(3) == 'Fizz'
    assert f.say(6) == 'Fizz'

    
def test_input_is_divisible_by_5_should_get_buzz():
    f = FizzBuzz()
    assert f.say(5) == 'Buzz'
    assert f.say(10) == 'Buzz'

    
def test_input_is_divisible_by_3_and_5_should_get_fizzbuzz():
    f = FizzBuzz()
    assert f.say(15) == 'FizzBuzz'
    assert f.say(30) == 'FizzBuzz'

    
def test_input_is_number_should_get_number():
    f = FizzBuzz()
    assert f.say(2) == 2
    assert f.say(7) == 7