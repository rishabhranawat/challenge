class Solution(object):
		def hIndex(self, citations):
			N = len(citations)
			if(N > 0): l = max(citations)+1
			else: l = 1
			index = [0]
			no_more_than_h = {}
			at_least_h = {}

			for i in range(0, l, 1):
				no_more_than_h[i] = 0
				at_least_h[i] = 0

			for citation_val in citations:
				for h, val in no_more_than_h.items():
					if(citation_val >= h):
						at_least_h[h] += 1
					elif(citation_val <= h):
						no_more_than_h[h] += 1

			for i in range(0, l, 1):
				h = i
				have_at_least_h = at_least_h[h]
				if(have_at_least_h >= h):
					have_no_more_than = no_more_than_h[h]
					if(have_no_more_than <= N-h):
						index.append(h)
			return max(index)

		def hIndex2(self, citations):
			N = len(citations)
			if(N > 0): l = max(citations)+1
			else: return 0
			index = [0]
			no_more_than_h_at_least = {}

			for i in range(0, l, 1):
				no_more_than_h_at_least[i] = [0, 0]

			for citation_val in citations:
				for h, val in no_more_than_h_at_least.items():
					if(citation_val >= h):
						no_more_than_h_at_least[h][1] += 1
					elif(citation_val <= h):
						no_more_than_h_at_least[h][0] += 1

			for i in range(0, l, 1):
				h = i
				have_at_least_h = no_more_than_h_at_least[h][1]
				if(have_at_least_h >= h):
					have_no_more_than = no_more_than_h_at_least[h][0]
					if(have_no_more_than <= N-h):
						index.append(h)
			return max(index)


a = Solution()
print(a.hIndex2([3, 0, 6, 1, 5]))
print(a.hIndex2([1, 1]))
print(a.hIndex2([0, 1]))