from itertools import permutations
text = "parth boy"
perms = permutations(text)
total = 0
for p in perms:
    print(''.join(p))
#     total += 1
# print(f"total number of permutation is: {total}")