def countClumps(arr, N):
	clumps = 0
	i = 0
	while(i < N - 1):
		flag = 0
		while (i + 1 < N and
			arr[i] == arr[i + 1]):
			flag = 1
			i += 1

		if (flag):
			clumps += 1
		i += 1
	return clumps
arr = [ 13, 15, 66, 66, 66,
		37, 37, 8, 8, 11, 11 ]
N = len(arr)
print("The no of clumps are:")
print(countClumps(arr, N))

