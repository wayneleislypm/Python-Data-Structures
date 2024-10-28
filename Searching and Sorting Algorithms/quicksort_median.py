def quick_sort(collection):
	if len(collection)<2:
		return collection
	m = len(collection)//2
	pivot = collection[m]
	collection.pop(m)
	lo = [x for x in collection if x <= pivot]
	hi = [x for x in collection if x > pivot]
	return quick_sort(lo) + [pivot] + quick_sort(hi)
l = [4, 67, 4,90, 6, 23, 67, 23, 78, 45, 12,1, 55, 88, 99, 239]
print(quick_sort(l))

