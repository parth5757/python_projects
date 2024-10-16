# Program to multiply two matrices using nested loops

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
#    print(len(X), i)
   # iterate through columns of Y
   for j in range(len(Y[0])):
    #    print(len(Y[0]), j)
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
        #    print('[i][j], [i][k], [k][j]', [i],[j], [i],[k], [k],[j])

for r in result:
   print(r)
