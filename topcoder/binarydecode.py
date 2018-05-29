class BinaryCode:
	
	def decodeHelper(self, s, assume):
		memo = {}
		memo[0] = int(assume)
		memo[1] = int(s[0])-int(memo[0])

		if(memo[1] != 1 and memo[1] != 0): return None
		for i in range(1,len(s)-1, 1):
			memo[i+1] = int(s[i])-int(memo[i-1])-int(memo[i])
			if(memo[i+1] != 1 and memo[i+1] != 0): return None
		r = ""
		for k, v in memo.items():
			r += str(v)
		return r

	def decode(self, s):
		ret = [None, None]
		ret = tuple(self.decodeHelper(s, "0"))
		print(ret)
		

		

a = BinaryCode()
print(a.decode("123210122"))
print(a.decode("11"))
print(a.decode("22111"))