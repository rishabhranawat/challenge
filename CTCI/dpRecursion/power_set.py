class PowerSet(object):

	def get_power_set(self, s):
		sets = []
		sets.append([])
		for element in s:
			element_subsets = []
			for subset in sets:
				new_subset = list(subset)
				new_subset.append(element)
				element_subsets.append(new_subset)
			sets.extend(element_subsets)
		return(sets, len(sets))

a = PowerSet()
print(a.get_power_set([1, 2, 3, 4]))



