import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if(k == 0): return []
        s = sorted(nums)
        prev = s[0]
        counter = 1
        hist = {}
        for i in range(1, len(s), 1):
            if(prev == s[i]):
                counter += 1
            else:
                if(counter in hist):
                    hist[counter].append(prev)
                else:
                    hist[counter] = [prev]
                prev = s[i]
                counter = 1
        if(counter in hist and prev not in hist[counter]):
            hist[counter].append(prev)
        else:
            hist[counter] = [prev]

        h = []
        for freq, vals in hist.items():
            times = len(vals)
            while(times > 0):
                heapq.heappush(h, freq*-1)
                times -= 1

        ret = []
        while(k > 0):
            n = heapq.heappop(h)
            n = n * -1
            v = hist[n][0]
            hist[n] = hist[n][1:len(hist[n])]
            ret.append(v)
            k -= 1
        return ret
a = Solution()
s = [4,1,-1,2,-1,2,3]
print(a.topKFrequent(s, 2))