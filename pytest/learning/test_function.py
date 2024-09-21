# Simple function to get the square number
def square(num):
    return num * num

#simple function find cubes of another
def cube(num):
    return square(num) * num

#Test the square function
#test must be start with "test_"

def test_square():
    num = 5
    result = square(num)
    assert result == num ** 2


#  this test function is for the cube function

def test_cube():
    nums = 5
    result = cube(nums)
    assert result == nums ** 3, "cube is not done"


test_cube()