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

# denoms = [25, 10, 5, 1]
# amount = 100
# a = []
# print(makeChange(a, amount, denoms, 0))
# print(a)


def change(amount, denoms):
	if(amount == 0): return 0
	else:
		mi = None
		for denom in denoms:
			val = change(amount-denom, denoms)

			if(mi == None or val < mi):
				mi = val
		return mi + 1


'''
C(P) = min_i{C(P-v_i)}+1
'''
import sys

def coinChange(amount, denoms):
	total = [sys.maxint-1]*(amount+1)
	coin_track = [-1]*(amount+1)

	total[0] = 0

	for i in range(0, len(total), 1):
		for j in range(0, len(denoms), 1):
			if(i >= j):
				if(total[i-denoms[j]]+1 < total[i]):
					total[i] = 1 + total[i-denoms[j]]
					coin_track[i] = j

	current_denom_index = coin_track[amount]
	current_denom_val = denoms[current_denom_index]
	acc = amount
	while(acc > 0):
		acc -= current_denom_val
		current_denom_index = coin_track[acc]
		current_denom_val = denoms[current_denom_index]
		print(current_denom_val)
		

	return total[amount]
print(coinChange(15, [1, 3, 5]))


