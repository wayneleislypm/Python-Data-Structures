def merge_sort(list):
	if len(list) < 2:
		return list
	m = len(list)//2
	return merge(merge_sort(list[:m]),merge_sort(list[m:]))

def merge(left, right):
		result = []
		i = j = 0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				result.append(left[i])
				i += 1
			else:
				result.append(right[j])
				j += 1
		result += left[i:]
		result += right[j:]
		return result
l = [4, 67, 4,90, 6, 23, 67, 23, 78, 45, 12,1, 55, 88, 99, 239]
print(merge_sort(l))
	