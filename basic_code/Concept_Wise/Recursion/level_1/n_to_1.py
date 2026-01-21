def print_n_to_1(n):
    if n == 1:
        return 1
    print(n)
    # print_n_to_1(n-1) # without return it just return the none value only.
    return print_n_to_1(n-1)

print(print_n_to_1(5))


