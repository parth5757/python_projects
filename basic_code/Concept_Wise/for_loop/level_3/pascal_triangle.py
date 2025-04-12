# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
n = 5
for i in range(n):
    num = 1
    for j in range(1, i + 2):
        print(num, end=" ")
        num = num * (i - j + 1) // j
    print()


#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
row = [1]
for i in range(1, n+1):
    # row with that required space
    print(" " * (n - i), end="")

    # print the current row
    for j in row:
        print(j, end=" ")
    print()

    # generate the new row
    new_row = [1]
    for k in range(1, len(row)):
        # print(new_row)
        new_row.append(row[k-1]+row[k])
    new_row.append(1)
    row = new_row