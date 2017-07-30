def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)/2
    start = 0
    mid = n
    end = len(nums) - 1
    min_sum = 1000000
    print(start, mid, end)
    while(mid < end):
        s = nums[start] + nums[mid]
        if(s < min_sum):
            min_sum = s
        start += 1
        mid += 1
        
    return min_sum
            
print(arrayPairSum([1, 4, 3, 2]))