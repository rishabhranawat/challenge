from collections import deque

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = deque()
        queue = deque()
        
        for letter in s:
            if(letter.isalnum()):
                l = letter.lower()
                stack.append(l)
                queue.append(l)
        
        while(len(stack) > 0 and len(queue) > 0):
            if(stack.pop() != queue.popleft()):
                return False
        return True

    def isPalindromeTwoPointers(self, s):

        start = 0
        end = len(s)-1
        n = len(s)

        while(start < end):

            first = s[start]
            while(not first.isalnum() and start < n-1):
                start += 1
                first = s[start]

            last = s[end]
            while(not last.isalnum() and end >= 1):
                end -= 1
                last = s[end]

            if(last.lower() != first.lower()):
                return False

            start += 1
            end -= 1
        return True


a = Solution()
print(a.isPalindromeTwoPointers("A man, a plan, a canal: Panama"))
print(a.isPalindromeTwoPointers("race a car"))
print(a.isPalindromeTwoPointers("aaabbb"))
print(a.isPalindromeTwoPointers("baab"))
print(a.isPalindromeTwoPointers("baoab"))

print(a.isPalindromeTwoPointers(".,"))