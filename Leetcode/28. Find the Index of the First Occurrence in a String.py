class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        for i in range(len(haystack) - len(needle)+1):
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1 