class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        new = ""
        for i in range(len(haystack) - len(needle)):
            print(i)
            if haystack[i] == needle[i]:
                store = i
                j = 0
                while j < len(needle):
                    if haystack[j+i] == needle[j]:
                        new += needle[j]
                    j+=1
                print(j)

haystack = "leetcode"
needle = "leeto"
print(Solution.strStr(Solution, haystack, needle))