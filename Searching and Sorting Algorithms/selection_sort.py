def selection_sort(list):
	for i in range(0, len(list)):
		min = i
		for j in range(i+1, len(list)):
			if list[j] < list[min]:
				min = j
		list[i], list[min] = list[min], list[i]
	print(list)
list = [2,5,1,6,8,3,4,9,23,12]
print(selection_sort(list))