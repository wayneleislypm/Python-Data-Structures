def binarySearch(array, value, left, right):
	if (left > right):
		return 'Not Found'
	middle = (left + right)//2
	if (array[middle] == value):
		return "Found and is at position: " + str(middle)
	elif (array[middle] > value):
		return binarySearch(array, value, left, middle-1)
	else:
			return binarySearch(array, value, middle+1, right)
			
list = [1,2,8,17,19,42]
print(binarySearch(list, 19, 0, len(list)-1))
			