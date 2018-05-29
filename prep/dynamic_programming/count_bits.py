class Solution(object):
	def countBits(self, num):
		"""
		:type num: int
		:rtype: List[int]
		"""
		memo = {}
		memo[0] = [0]
		memo[1] = [1]
		
		counted = 2
		i = 2
		while(counted <= num+1):
			memo[i] = memo[i-1]+[x+1 for x in memo[i-1]]
			counted += len(memo[i])
			i += 1

		res  = []
		counter = 0
		
		for k, v in memo.items():
			if(len(res) == num+1): return res
			elif(len(res)+len(v) <= num+1):
				res.extend(v)
			else:
				i = 0
				while(len(res) <= num):
					res.append(v[i])
					i += 1
		return res

a = Solution()
print(a.countBits(64))


