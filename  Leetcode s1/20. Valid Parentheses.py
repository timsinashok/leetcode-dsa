class Solution:
    def isValid(self, s: str) -> bool:
        closing = {'[' : ']', '(' : ')', '{' : '}'}

        if(s[0] in closing.values()):
            return False

        data = []

        for i in range(len(s)):
            #print(s[i])
            if s[i] in list(closing.keys()):
                data.append(s[i])
            elif s[i] in list(closing.values()):
                if (len(data) == 0):
                    return False
                elif (closing[data[-1]] == s[i]):
                    data.pop()
                else:
                    return False
            
        if (len(data) == 0):
            return True
        else:
            return False