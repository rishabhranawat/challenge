def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    index_1 = 0
    index_2 = 1
    i = 0
    n = len(numbers)
    s = numbers[index_1] + numbers[index_2]
    while(s != target):
        s = numbers[index_1] + numbers[index_2]
        if(s == target): break
        print(s, target, index_1, index_2)
        if(s > target):
            index_1 += 2
        else:
            index_2 += 1
    return index_1+1, index_2+1

print(twoSum([2, 7, 11, 15], 9))