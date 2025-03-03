# Suppose there there is big farm land that land divided into different parts and each represent in form of in form of 0's & 1's in matrix form. now here 0 means bad area and 1 means good area and here you have to find maximum square of good area that can farm by farmer.

# the Example of total land in give following matrix form

# 0 1 1 0 1
# 1 1 0 1 0
# 0 1 1 1 0
# 1 1 1 1 0
# 1 1 1 1 1
# 0 0 0 0 0


class maximum_area():
    def find_max_area(self, farm):
        if not farm:
            return 0
        for i in range(len(farm)):
            for j in range(len(farm[i])):
                # print(f"Element at row {i}, column {j} is {farm[i][j]}")
                # logic for the element value which is one that check all of that right left down and up element value
                if farm[i][j] == 1:
                    print(f"found value {1} at {i},{j}")
                    if farm[i][j+1] == 1:
                        print(f"valid at {i},{j}")

farm = [[0, 1, 1, 0, 1], [1, 1, 0, 1, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
square_farm = maximum_area()
print(square_farm.find_max_area(farm))