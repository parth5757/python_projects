x = 10

def update():
    global x
    x += 5
update()
print(x)

# Let we do without global and see what happen here

x = 10
def update():
    # global x
    # let we think we can declare same name local variable with the anothe given value. And see what happen ?
    x = 4
    x += 5
    return x
# it will print here the 9 value becuase now it only work with the local x variable. & do there related operations.
print(update())
print(x)

# It shows following error that unboundLocalError. And you can't update it.
#     x += 5
#     ^
# UnboundLocalError: cannot access local variable 'x' where it is not associated with a value