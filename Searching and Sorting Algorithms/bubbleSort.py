def bubbleSort(list):
	i = len(list)
	while i > 0:
		i -= 1
		for j in range(0, i):
			if list[j] > list[j+1]:
				list[j], list[j+1] = list[j+1], list[j]
	print(list)
list = [2,5,1,6,8,3,4,9,23,12]
bubbleSort(list)