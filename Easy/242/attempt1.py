# my own solution
# o(n) + o(n) + o(n) = o(n)
# memory complexity: worst case: o(n)
# best case: o(1)

# loop over two strings and add to its own dict that counts each unique string
# compare dict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 
        dict1={'':0}
        dict2={'':0}
        for char in s: # O(n)
            if char in dict1:
                dict1[char]+=1
            else:
                dict1[char] = 1
        for char in t: # O(n)
            if char in dict2:
                dict2[char]+=1
            else:
                dict2[char] = 1 
        if dict1==dict2: # O(n)
            return True
        else:
            return False