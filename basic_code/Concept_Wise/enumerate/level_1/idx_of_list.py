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