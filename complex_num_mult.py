# Problem Source: LeetCode
# Given two strings representing two complex numbers.

# You need to return a string representing their multiplication. 
# Note i2 = -1 according to the definition.

# Example 1:
# Input: "1+1i", "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, 
# and you need convert it to the form of 0+2i.
# Example 2:
# Input: "1+-1i", "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, 
# and you need convert it to the form of 0+-2i.
# Note:

# The input strings will not have extra blank.
# The input strings will be given in the form of a+bi, where the integer a 
# and b will both belong to the range of [-100, 100]. And the output should be also in this form.

### ### ###
def complexNumberMultiply(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    a_dets = a.split("+")
    b_dets = b.split("+")
    a_real = a_dets[0]
    b_real = b_dets[0]
    a_img = a_dets[1]
    b_img = b_dets[1]

    real_real = int(a_real)*int(b_real)
    real_img = int(a_real)*int(b_img.replace("i", ""))

    img_real = int(b_real)*int(a_img.replace("i", ""))
    img_img = int(b_img.replace("i", ""))*int(a_img.replace("i", ""))

    ret_str = str(real_real+(img_img*-1))+"+"+str(real_img+img_real)+"i"
    return ret_str



a = "1+-1i"
b = "0+0i"
print(complexNumberMultiply(a, b)) 