class PermuationWithDups(object):

	def perms_dups(self, s):
		perms = [""]
		for i in s:
			perms = self.perms_helper(i, perms)
		p = set(perms)
		return p, len(p)
	def perms_helper(self, s, perms):
		new_perms = []
		for each in perms:
			for i in range(-1, len(each)+1, 1):
				new = each[:i+1]+s+each[i+1:]
				new_perms.append(new)
		return new_perms


a = PermuationWithDups()
print(a.perms_dups("abcde"))
print(a.perms_dups("abc"))