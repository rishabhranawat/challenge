'''
Write a function to swap a number in place

I had to look this trick up, dang.
'''
def swap(m, n):
	print(m, n)
	m = m^n
	n = m^n
	m = m^n
	print(m, n)
swap(10, 15)