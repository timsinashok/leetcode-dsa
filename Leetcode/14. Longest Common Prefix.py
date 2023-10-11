class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if(len(strs) == 1):
            return strs[0]

        min = len(strs[0])
        ans = ''
        for i in range(1, len(strs)):
            if(len(strs[i]) < min):
                min = len(strs[i])
        
        if(min == 0):
            return ans
        
        j = 0
        
        while(j<min):
            a = strs[0][j]
            c = 0
            for i in range(1,len(strs)):
                if(strs[i][j] != a):
                    return ans
            ans = ans + a
            j = j+1
        return ans

            