import sys
class Solution:
	def minWindow(self, s, t):
		window = {}
		start = 0
		end = 0
		mi = sys.maxint-1
		window_size = len(t)
		miv = ""
		for letter_t in t:
			if(letter_t in window):
				window[letter_t] += 1
			else:
				window[letter_t] = 1

		while(end < len(s)):
			right_edge = s[end]

			if(right_edge in t):
				if(window[right_edge] >= 0):
					window[right_edge] -= 1
					window_size -= 1
			end += 1

			while(window_size == 0):
				if(mi > end-start):
					miv = s[start:end]
					mi = min(mi, end-start)

				left_edge = s[start]
				if(left_edge in window):
					window[left_edge] += 1
					window_size += 1
				start += 1
		return miv

s = "abab"
t = "aaa"
a = Solution()
print(a.minWindow(s, t))

			
