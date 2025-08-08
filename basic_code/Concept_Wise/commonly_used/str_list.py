s = "Jay Shree Ram"
# convert in list
s_list = list(s)
print(s_list)

# now here add ignore any given value thing
s_list = []
for i in range(len(s)):
    if(s[i] != " "):
        s_list.append(s[i])

print(s_list)

# convert backto string
result = ''.join(s_list)
print(result)