# #square function
def square(num):
    return num * num

# 
def test_square(initial_value):
    print(f"Running Test: {initial_value}")
    result = square(initial_value)
    print(f"yield fixture generated result: {result}")
    assert result == initial_value ** 2
