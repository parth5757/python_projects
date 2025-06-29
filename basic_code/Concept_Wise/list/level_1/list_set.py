lst = [[1,2,3], [4,5,6], [7,8,9]]
try:
    print(set(lst))
except TypeError:
    print("Opps, here thr unhashable type: list error(nested list can't be convert into the set.)")


# method 2

nested_list = [[1,2,], [3,4,], [5,6]]
flattened_list = [item for sun_item in nested_list for item in sun_item]
print(set(flattened_list))