def fibonacci(n):
    if n == 1:
        return 1
    else:
        return n + fibonacci(n-1)

print(fibonacci(5))


# 5+4+3+2+1=15