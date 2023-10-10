class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # dict for conversion
        roman_dict = {'L' : 50, 'C':100, 'D': 500, 'M': 1000, 'I':1, 'V':5, 'X':10}
        num = 0
        l = 0
        while(l<len(s)):
            if(l == len(s)-1):
                num = num + roman_dict[s[l]]
                break
            else:
                if(roman_dict[s[l]] < roman_dict[s[l+1]]):
                    num = num + roman_dict[s[l+1]] - roman_dict[s[l]]
                    l = l+2
                else:
                    num = num + roman_dict[s[l]] 
                    l = l + 1
                
        return num
            
            


        