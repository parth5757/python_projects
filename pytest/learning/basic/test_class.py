def square(num):
    return num * num
def cube(num):
    return square(num) * num


# our class contain our tests methods
# Notes: Must start with 'Test'

class TestClass:
    # make common instance name between two function\
    num = 5 # this thing will make num memory only once
    
    def test_square(self):
        result = square(self.num)
        assert result == self.num ** 2

    def test_cube(self):
        result = cube(self.num)
        assert result == self.num ** 3, "cube is not done"