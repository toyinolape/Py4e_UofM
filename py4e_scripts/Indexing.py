import numpy

#indexing
arr = numpy.arange(0,12)
print(arr)

print(arr[0])#first charcheter in array
print(arr[1])#second charcheter in array
print(arr[2])#third charcheter in array

print(arr[0:5])#from first charcter to 5th character excluding the fifth

arr[0:5] = 20 #assigns the first 5 elements to 20

arr2 = arr[0:6]
print(arr2)

