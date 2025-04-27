"""
Solution; 
1. strip all the whitespace characters
stripping does not work 
so lets put in list by comparing each character ifhtey are alpha
2. find length
3. use tow pointer and move left and right and ompare
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        for ch in s:
            if ch.isalnum():
                a.append(ch.lower())

        # return a[::-1] == a 
        l = 0
        r = 0
        if len(a) % 2 ==0:
            l = len(a) // 2 - 1
            r = l + 1
        else:
            r = l = len(a) // 2
        
        while l >= 0:
            if a[l] == a[r]:
                pass
            else:
                return False
            l -= 1
            r += 1
        return True



                

        
        