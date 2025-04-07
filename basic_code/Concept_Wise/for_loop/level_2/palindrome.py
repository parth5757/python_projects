input_str = input("enter anything you want: ")
# method 1
print("method 1")
new_str = input_str[::-1] 
if input_str == new_str: 
    print(True)
else:
    print(False)

# method 2
print("method 2")
lst_str = []
for i in range(len(input_str)-1, -1, -1): # reverse for loop concept here use 
    print(input_str[i])
    lst_str.append(input_str[i])
    # print(lst_str)
new_str = ''.join(lst_str)
if input_str == new_str:
    print(True)
else:
    print(False)

# method 3
print("method 3")
length = len(input_str)
# if(len(input_str) % 2 == 0):
#     length = len(input_str) + 1
for i in range(length):
    print(input_str[i], i, input_str[-1-i], -1-i)
    if input_str[i] != input_str[-1-i]:
        print(input_str, 'is not palindrome')
        break
else:
    print(input_str, "is palindrome.")