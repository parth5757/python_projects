def pyramid(n):
    for i in range(n):
        for j in range(n- i - 1):
            print(" ", end="")
        for k in range(i + 1):
            if k == range(i + 1):
                print('*', end='')
            else:
                print('* ', end='')
        print()
        
n = int(input("enter number you want:"))
pyramid(n)


# def pyramid(n):
#     for i in range(n):
#         print("*" * (n - i -1), end="")
#         print("*" * (i + 1))
# pyramid(5)