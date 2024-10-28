def binarySearch(list, target):
	first = 0
	last = len(list)-1
	
	while first <= last:
		midpoint = (first+last)//2
		if list[midpoint] == target:
			return (str(target) +' is at index ' + str(midpoint))
		elif list[midpoint] < target:
			first = midpoint + 1
		else:
			last = midpoint - 1
	return None
list = [1,2,8,17,19,42]
print(binarySearch(list, 42))