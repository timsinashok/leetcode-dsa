"""
Solution:
use stack
if opening addd to stack
closing remove from stack:
"""

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        brackets = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets.keys():
                if stack and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
        return False if stack else True