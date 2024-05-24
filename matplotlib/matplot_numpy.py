import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints)
# plt.show()


# use o for represnt in chart

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints, 'o')
# plt.show()

# enter 2 specific side value in array

# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(xpoints, ypoints)
# plt.show()


# single axis input only

# ypoints = np.array([3, 8, 1, 10, 5, 7])

# plt.plot(ypoints)
# plt.show()


# use "o" or "*" to represent that

# ypoints = np.array([3,8,1,10])

# plt.plot(ypoints, marker = '*')
# plt.show()



# # for red color 

# ypoints = np.array([3,8,1,10])

# plt.plot(ypoints, 'o:r')
# plt.show()

#  change the size of marker

ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = 'o', ms = 20)
# plt.show()


# change color of marker
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
# plt.show()

# plt.plot(ypoints, linestyle = 'dotted')
# # much more shorter way for this
# # plt.plot(ypoints, ls = ':')
# plt.show()


# # simple color line
# plt.plot(ypoints, color = 'r') # at color you can use any color ans also use the color code
# plt.show()

# for line width

plt.plot(ypoints, linewidth = '20.5')
plt.show()