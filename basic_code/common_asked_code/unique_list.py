str = ["a","b","c","a","b","c"]

uniq_str = []

for i in range(len(str)):
    if str[i] not in uniq_str:
        uniq_str.append(str[i])

print(uniq_str)
