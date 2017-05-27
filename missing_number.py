# Problem Source: LeetCode
# Given an array containing n distinct numbers taken 
# from 0, 1, 2, ..., n, find the one that is missing from the array.

# For example,
# Given nums = [0, 1, 3] return 2.

# Note:
# Your algorithm should run in linear runtime complexity. 
# Could you implement it using only constant extra space complexity?

### ### ###

def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(0, len(nums), 1):
        if(i != nums[i]): return i
    return -1

print(missingNumber([0, 1, 2, 4]))