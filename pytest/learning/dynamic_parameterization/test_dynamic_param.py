# square function
def square(num):
    return num * num

# fixture function

def test_square(initial_value):
    result = square(initial_value)
    assert result == initial_value ** 2