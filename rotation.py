#!/usr/env/bin/python

# Array Rotation, using pop, to get the elements and then keeping them in a separate list and then appending at the end of the array


from array import array

arr = array('i', [1, 2, 3, 4, 5, 6, 7])
n = 7
d = 2
tmp = []

for i in range(d):
	tmp.append(arr.pop(0))
arr.extend(tmp)
print(arr)
