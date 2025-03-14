class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c if c.isalnum() else '' for c in s).lower()   
        if s == s[::-1]: # originally search through the first half and the 2nd half
            return True
        else: return False