def outer():
    global x
    x = 10
    def inner():
        x += 5
        return x
    return inner()

# print(outer())

# here let am i do with the nonlocal
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        return x
    return inner()

print(outer())