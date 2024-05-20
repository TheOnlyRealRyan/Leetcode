class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        new = s.split()
        return new[len(new)-1]
        # print(new)
        
        
        
s = "Hello World"
s = "   fly me   to   the moon  "
if __name__ == "__main__":
    print(Solution.lengthOfLastWord(Solution, s))