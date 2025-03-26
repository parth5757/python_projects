# Print Each Character of a String
# Method 1
print("Method 1")
text = "Hare Ram Hare Krishna"
for char in text:
    print(char)

# Method 2
print("Method 2")
text = "Hare Ram Hare Krishna"
ans = list(text)
for char in ans:
    print(char)
# # OR Directly like this
# for char in list(text):
#     print(char)

# Method 3
print("Method 3")
text = "Hare Ram Hare Krishna"
for i in range(len(text)):
    print(text[i])

# Method 4
print("Method 4")
text = "Hare Ram Hare Krishna"
for i ,val in enumerate(text):
    print(val)