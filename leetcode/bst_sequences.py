class TreeNode:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None


def weave(first, second, results, prefix):
	if(len(first) == 0 or len(second) == 0):
		result = [x for x in prefix]
		result.extend(first)
		result.extend(second)
		results.append(result)
		return

	hFirst = first.pop(0)
	prefix.append(hFirst)
	weave(first, second, results, prefix)
	prefix.pop()
	first = [hFirst]+first

	sFirst = second.pop(0)
	prefix.append(sFirst)
	weave(first, second, results, prefix)
	prefix.pop()
	second = [sFirst]+second

def allSequences(node):
	result = []

	if(node == None): 
		result.append([])
		return result

	prefix = []
	prefix.append(node.val)

	left = allSequences(node.left)
	right = allSequences(node.right)

	print(left, right)

	for l in left:
		for r in right:
			weaved = []
			weave(l, r, weaved, prefix)
			result.extend(weaved)
	return result


t50 = TreeNode(50)
t20 = TreeNode(20)
t60 = TreeNode(60)
t10 = TreeNode(10)
t25 = TreeNode(25)
t70 = TreeNode(70)
t55 = TreeNode(55)

t20.left = t10
t20.right = t25

t60.right = t70
t60.left = t55

t50.left = t20
t50.right= t60

print(allSequences(t50))
