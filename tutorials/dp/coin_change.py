def makeChange(a, amount, denoms, index):
	if(index >= len(denoms)-1): return 1

	denomAmount = denoms[index]
	ways = 0
	i = 1
	while(i*denomAmount <= amount):
		remaining = amount - (i*denomAmount)
		ways += (makeChange(a, remaining, denoms, index+1))
		i+=1
	a.append(ways+1)
	return ways

denoms = [25, 10, 5, 1]
amount = 100
a = []
print(makeChange(a, amount, denoms, 0))
print(a)