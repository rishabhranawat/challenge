# Problem Source: LeetCode

# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), 
# some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]

### ### ###

def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums = sorted(nums)
    first = 0
    second = 1
    twice = []
    while(second < len(nums)):
        if(nums[first] == nums[second]):
            twice.append(nums[second])
            first += 2
            second += 2
        else:
            first += 1
            second += 1
    return(twice)
print(findDuplicates([4,3,2,7,8,2,3,1]))