def sequentialSearch(list, item):
	for i in range(len(list)):
		if list[i] == item:
			return 'Found and is at position: ' + str(i)
	return 'Not Found'
L = [1,2,34,5,6,8]
print(sequentialSearch(L, 2))