class TreeNode:
	def __init__(self, val, level):
		self.val = val
		self.level = level
		self.children = []
		self.parent = None

def longestfp(s):
	cpath = ""
	maxpath = ""
	prev_directory = []
	current_level = 0
	number_tabs = 0
	types = ["\n", " ", "\t"]

	i = 0
	while(i < len(s)):
		val = s[i]
		if(val == "\n"):
			temp_level = 0
			i += 1
			val = s[i]
			while(val in types):
				temp_level += 1
				i += 1
				val = s[i]

			if(temp_level <= current_level):
				prev_directory = prev_directory[:temp_level]
				cpath = "/".join(prev_directory)+"/"
				current_level = temp_level
			else:
				current_level += 1
				
		next_file = ""
		while(i < len(s) and val not in types):
			next_file += val
			i += 1
			if(i >= len(s)): break
			val = s[i]

		if("." not in next_file):
			prev_directory.append(next_file)
			cpath += next_file+"/"
		else:
			fp = cpath + next_file
			if(len(fp) > len(maxpath)):
				maxpath = fp
	return maxpath				


s = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
s = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
s = "dir\n\tfile.txt"
s = "dir\n        file.txt"
print(len(longestfp(s)))