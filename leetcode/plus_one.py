class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        add =  True
        i = len(digits)-1
        while(add and i >= 0):
            if(1 + digits[i] >= 10):
                digits[i] = (1+digits[i])%10
            else:
                digits[i] = (1+digits[i])
                add = False
            i -= 1
        if(add):
            return [1]+digits
        return digits

    def plusOne(self, digits):
        return int("".join(digits))+1

a = Solution()
print(a.plusOne([1, 2, 3]))
print(a.plusOne([9,9,9]))
print(a.plusOne([1, 1, 9]))