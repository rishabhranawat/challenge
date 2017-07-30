def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    pairs ={}
    for each in nums:
        if(each in pairs):
            pairs[each] += 1
        else:
            pairs[each] = 1
    import operator
    sorted_x = sorted(pairs.items(), key=operator.itemgetter(0))

    coutn = 0
    ret = []
    for each in sorted_x:
        if(len(ret)==k): break
        ret.append(each[0])
    return ret
   
print(topKFrequent([-1, -1], 2))
    