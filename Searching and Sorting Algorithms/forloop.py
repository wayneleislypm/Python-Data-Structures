x=(1,2,3,4,5,6,7,8,9)
odd=0
even=0
for e in x:
	if e%2:
		odd+=1
	else:
		even+=1
print(odd)
print(even)