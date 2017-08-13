class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        n_str = str(n)
        if(len(n_str) == 0): return ""

        curr_counter = 1
        counter = 1
        prev_letter = n_str[0]
        ret_str = ""
        while(counter < len(n_str)):
            letter = n_str[counter]
            if(prev_letter != letter):
                if(curr_counter == 1):
                    ret_str += str(prev_letter)
                else:
                    ret_str += str(curr_counter)+str(prev_letter)
                curr_counter = 1
                prev_letter = n_str[counter]
            else:
                curr_counter += 1
            counter += 1
        if(curr_counter == 1):
            ret_str+=str(prev_letter)
        else:
            ret_str += str(curr_counter)+str(prev_letter)
        return ret_str
a = Solution()
print(a.countAndSay(1))