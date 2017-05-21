# Problem Source: LeetCode
# Given an array nums, write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.

# For example, given nums = [0, 1, 0, 3, 12], 
# after calling your function, nums should be [1, 3, 12, 0, 0].

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

### ### ###

# O(2n)
def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    nz_indices = []
    for i in range(0, len(nums), 1):
        if(nums[i] != 0): nz_indices.append(i)

    counter = 0
    for j in range(0, len(nums), 1):
        if(counter != len(nz_indices)):
            nums[j] = nums[nz_indices[counter]]
            counter += 1
        else:
            nums[j] = 0

#O(n)
def moveZeroes2(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    zi = -1
    for i in range(0, len(nums), 1):
        if(nums[i] == 0 and zi == -1):
            zi = i
        if(nums[i] != 0 and i != zi and zi != -1):
            nums[zi] = nums[i]
            nums[i] = 0
            zi += 1
    print(nums)
                    
print(moveZeroes2([2, 1]))
            
                