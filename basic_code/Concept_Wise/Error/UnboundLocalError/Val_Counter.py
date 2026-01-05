# it's an prime example of the When you can get the UnboundLocalError

import inspect
count = 0

def inc():
    global count # if you not declare the global variable and try to use the same name variable in local function then it gives UnboundeLocalError
    count += 1
    # return count

def make_counter():

    # def inc():
    #     count += 1

    for i in range(10):
        inc()
    
    return count
    
# if __name__ == "__main__":
#     print(make_counter)

# ans = make_counter
# print(ans())

print(make_counter())

# help(make_counter)

# print(inspect.getsource(make_counter))