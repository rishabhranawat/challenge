class Solution(object):

	def convertThreeDigits(self, num):
		terms = {0:"", 1: "One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine",
		10: "Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen",
		17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty",
		70:"Seventy", 80:"Eighty", 90:"Ninety", 100:"Hundred"}

		num_str = ""
		div = 10
		place_div = 10
		while(num > 0):
			left = num % div
			place = div/place_div
			temp = int(str(num)[-2:])
			done = False
			if(temp in terms and  terms[temp] != "" and terms[temp] != "Ten" and terms[temp] != "One" and terms[temp] != "Hundred"): 
				num_str = terms[temp]+" "+num_str
				num -= temp
				div *= 10
				place_div *= 10
				done = True
			elif(terms[place] == "Ten"):
				num_str = terms[left]+" "+num_str
			elif(terms[place] == "Hundred"):
				num_str = terms[left/place]+" Hundred"+" "+num_str
			else:
				num_str = terms[left/place]+" "+ num_str
			div *= 10
			if(not done): num = num - left
		return num_str.strip()
			
	def numberToWords(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		if(num == 0): return "zero"
		units = {0:"", 1:"Thousand", 2:"Million", 3:"Billion"}
		num_str = ""
		start = None
		end = -3
		num = str(num)
		curr = num[end:start]
		counter = 0
		while(len(curr) > 0):

			num_str = self.convertThreeDigits(int(curr))+" "+units[counter]+" "+num_str 
			if(start == None): 
				start = -3
			else: start = end
			end -= 3
			curr = num[end:start]
			counter += 1
		return num_str.strip()

a = Solution()
print(a.numberToWords(1758))
print(a.numberToWords(202))
