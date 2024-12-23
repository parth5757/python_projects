# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

input_number = input("enter number")
lst = []
for i in range(1, int(input_number)+1):
    lst.append(i)

print(lst)