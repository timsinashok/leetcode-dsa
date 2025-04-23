"""
Solution:
1. Bruteforce try removing different 3 digits, nx(n-1)x(n-2) = O(n3) crazy
2. Stack
so start and input digit to stack 
if digit is greater than last digit on stack remove 
and if more digits needs to be removed , remove
"""

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        if len(num) == 0:
            return 0

        if k > len(num):
            return 0

        numbers = []
        for digit in num:
            while numbers and numbers[-1] > digit and k > 0:
                numbers.pop()
                k -= 1
            numbers.append(digit)

        numbers = numbers[:-k] if k > 0 else numbers
        result = "".join(numbers)
        result = result.lstrip("0")
        return result if len(result) > 0 else "0"