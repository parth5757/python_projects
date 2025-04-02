# Method 1
print("method 1")
text = "Python"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
    # print(reversed_text, char, reversed_text) # for reference only how it working
print(reversed_text)

# Method 2
print("method 2")
text = "python"
rev_txt = ""
for i in range(len(text), 0, -1):
    rev_txt += text[i-1]
print(rev_txt)

# Method 3
print("method 3")
text = "python"
rev_txt = ""
for i in reversed(text):
    rev_txt += i
print(rev_txt)

# Method 4
print("method 4")
text = "python"
rev_txt = ""
for i in range(len(text)):
    print(len(text), 1, i)
    rev_txt += text[len(text) - 1 -i]
print(rev_txt)