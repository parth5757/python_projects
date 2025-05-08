# print index of given list value
# method 1
print("method 1")
items = ['laxmi', 'sarswati', 'anapurna']
for idx, val in enumerate(items):
    print(idx, val)

# method 2
print("method 2")
for i in (enumerate(items, start=1)):
    idx = i[0]
    val = i[1]
    print(idx, val)

# method 3
print("method 3")
a = enumerate(items)
list(map(lambda i: print(i[0], i[1]), filter(lambda i: i[0] % 2 == 0 or i[0] % 2 != 0, a)))