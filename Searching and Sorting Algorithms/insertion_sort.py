def insertion_sort(list):
	for i in range(1, len(list)):
		value = list[i]
		j = i
		while j>0 and list[j-1]>value:
			list[j] = list[j-1]
			j -= 1
		list[j] = value
	return list
l = [4, 67, 4,90, 6, 23, 67, 23, 78, 45, 12,1, 55, 88, 99, 239]
print(insertion_sort(l))		
	
