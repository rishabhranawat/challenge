class Solution:
	def get_sub(self, s):
		window = {}
		start = 0
		end = 0
		max_len = 0 
		window_size = 0

		while(end < len(s)):
			right_edge = s[end]
			if(right_edge in window): 
				window[right_edge] += 1
			else: 
				window[right_edge] = 1
			
			if(window[right_edge] == 1):
				window_size += 1

			end += 1

			while(window_size > 2):
				left_edge = s[start]
				window[left_edge] -= 1
				if(window[left_edge] == 0):
					window_size -= 1
				start += 1

			max_len = max(max_len, end-start)
		return max_len

a = Solution()
print(a.get_sub("eceba"))