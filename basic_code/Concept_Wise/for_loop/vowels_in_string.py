# Method 1

print("Method 1")
text = "Hare Ram Hare Krishna"
# text = "hello world"
vowel = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowel:
        count += 1
print(count)


# Method 2
print("Method 2")
# text = "Jay Mahakal"
vowel = "aeiouAEIOU"
count = 0
ans = [char for char in text if char in vowel]
count = len(ans)
print(count)

# Method 3
print("Method 3")
# text = "Jay Swaminaryan"
vowel = "aeiouAEIOU"
count = sum(1 for char in text if char in  vowel)
print(count)


# Method 4
print("Method 4")
# text = "radha radha"
vowel = "aeiouAEIOU"
ans = list(filter(lambda char: char in vowel, text))
count = len(ans)
print(count)


# else way you use with filter at there remove the for instead of list where take loop in ans 