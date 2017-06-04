def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    l = [0]*(max(nums)+1)
    for each in nums:
        print(each)
        l[each] += 1
    l = sorted(l)
    return (l[len(l)-k:len(l)])
print(topKFrequent([1,1,1,2,2,3], 2))
    