# Problem Source: LeetCode

# Given an array of size n, find the majority element. 
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and 
# the majority element always exist in the array.

### ### ###

# Throws memory error also will only work
# for ints from 0 to max
def majorityElement1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_num = max(nums)
    n = len(nums)
    nums_a = [0]*(max_num+1)
    
    for i in range(0, n, 1):
        nums_a[nums[i]] = nums_a[nums[i]]+1
    return nums_a[nums_a.index(max(nums_a))]


# This works. Not too efficient
def majorityElement2(nums):
    counts = {}
    for number in nums:
        if(number in counts):
            counts[number] += 1
        else:
            counts[number] = 1

    maj_number = -1
    maj_count = 0
    for number, count in counts.items():
        if(count > maj_count):
            maj_count = count
            maj_number = number
    return maj_number