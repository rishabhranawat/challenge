class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        end = len(digits)-1
        carry = 1
        while(end >= 0):
            curr = digits[end] + carry
            if(curr >= 10):
                carry = 1
                digits[end] = 0
            else:
                carry = None
                digits[end] = curr
                return digits
            end -= 1

        return [1] + digits
                
a = Solution()
print(a.plusOne([1, 2, 3]))
print(a.plusOne([1, 2, 9]))
print(a.plusOne([9, 9, 9]))
print(a.plusOne([8, 9, 9]))
print(a.plusOne([1, 2, 3]))
print(a.plusOne([4,3,2,1]))