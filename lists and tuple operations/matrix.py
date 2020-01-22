X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
print("Original Matrices are:")
print("X: ")
for r in X:
   print(r)
   
print("\nY: ")
for r in Y:
   print(r)

added= [[0,0,0],
         [0,0,0],
         [0,0,0]]

multiplied= [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        added[i][j] = X[i][j] + Y[i][j]
       
        
for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           multiplied[i][j] += X[i][k] * Y[k][j]
          
print("\nThe added matrix is:")
for r in added:
   print(r)
  
print("\nThe Multiplied matrix is:")
for r in multiplied:
   print(r)
