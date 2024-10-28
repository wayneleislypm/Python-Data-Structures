def hanoi(n, A, B, C):
	if n == 1:
		print('Move disk', n, 'from', A, 'to', C)
	else:
		hanoi(n-1, A, C, B)
		print('Move disk', n, 'from', A, 'to', C)
		hanoi(n-1, B, A, C)
		
n = 3
hanoi(n, 'A', 'B', 'C')
		