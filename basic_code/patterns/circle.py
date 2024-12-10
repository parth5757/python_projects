# # #circle pattern code

# import math

# def draw_circle_pattern(radius):
#     # Calculate the diameter
#     diameter = 2 * radius

#     # Iterate over each row
#     for y in range(diameter + 1):  # Add 1 to include the bottom edge
#         # Iterate over each column
#         for x in range(diameter + 1):  # Add 1 to include the right edge
#             # Calculate the distance from the center
#             distance = math.sqrt((x - radius) ** 2 + (y - radius) ** 2)
            
#             # Print '*' if the distance is approximately equal to the radius
#             if radius - 0.5 < distance < radius + 0.5:
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#         print()

# # Draw a circle pattern with a specified radius
# draw_circle_pattern(10)


# import math
# def circle_star(radius):
#     diameter = 2 * radius

#     for y in range(diameter + 1):
#         # print(y)
#         for x in range(diameter + 1):
#             # print(x)
#             distance = math.sqrt((x - radius) ** 2 + (y - radius) ** 2)
#             # print(distance)
            
#             if radius - 0.5 < distance < radius + 0.5:
#                 print("*", end='')
#             else:
#                 print(' ', end='')
#         print()
# circle_star(10)

import math

def circle_star(radius):
    diameter = 2 * radius

    for y in range(diameter + 1):
        for x in range(diameter + 1):
            distance = math.sqrt((x - radius) ** 2 + (y - radius) ** 2)
            
            # Adjust tolerance for a smoother circle appearance
            if abs(distance - radius) < 0.5:
                print("*", end='')
            else:
                print(' ', end='')
        print()

circle_star(10)
