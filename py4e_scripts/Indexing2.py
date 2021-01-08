import numpy

arr2d = numpy.array([[1,2,3],[4,5,6],[7,8,9]]) #creating a 2 dimensional array

print (arr2d)
#print (arr2d[0][2])

#slices of 2d array

slice1 = arr2d[0:1,0:2]
#print(slice1)

#arr2d[:2,1:] = 15
#print arr2d

#using loops to index
arr_len = arr2d.shape[0]

for i in range(arr_len):
    arr2d[i] = i;

#print(arr2d)

#Accessing rows

print( arr2d[[0,1]])
print(arr2d[[1,0]])
