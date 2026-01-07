# This logic is completely wrong and not work. That we have to know that we can't update the count variable value.
# count = 0

# def add():
#     global count
#     count += 1

# def sub():
#     global count
#     count -= 1


# same thing with different wat we can do as like showing herew
class Counter:
    def __init__(self, start=0):
        self.count = start

    def add(self, x):
        self.count += x
        
    def subtract(self, x):
        self.count -= x

    def multiply(self, x):
        self.count *= x

    def value(self):
        return self.count
    

c = Counter(10)

c.add(5)        # 15
c.subtract(3)   # 12
c.multiply(2)   # 24

print(c.value())


# We can also use here the nonlocal to do same thing



def make_counter(start=0):
    count = start

    def add(x):
        nonlocal count
        count += x
        return count

    def sub(x):
        nonlocal count
        count -= x
        return count
    
    # def mul(x):
    #     nonlocal count
    #     count *= x
    #     return count
    
    # def div(x):
    #     nonlocal count
    #     count /= x
    #     return count
    
    def get():
        return count
    
    # return add, sub, div, mul, get  # if we use here this then it gives ValueError
    return add, sub, get



add, sub, get = make_counter(10)

add(5)   # 15
sub(2)   # 13
print(get())
