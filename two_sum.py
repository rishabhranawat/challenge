def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    original = nums
    nums = sorted(nums)
    start = 0
    end = len(nums)-1
    while(start <= end):
    	temp = nums[start] + nums[end]
    	if(temp == target): 
    		first = original.index(nums[start])
    		original[first] = -1
    		second = original.index(nums[end])
    		original[second] = -1
    		return [first, second]
    	elif(temp < target):
    		start += 1
    	else:
    		end -= 1
    return None



print(twoSum([3, 3], 6))