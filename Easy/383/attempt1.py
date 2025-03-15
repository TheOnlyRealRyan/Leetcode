# My own solution
# adds the 2 strings to its own dict and compares the values
# values of dict_ransomNote should be <= values of dict_magazine
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_ransomNote = {}
        dict_magazine = {}
        for char in ransomNote: # o(N)
            if char in dict_ransomNote:
                dict_ransomNote[char] +=1
            else:
                dict_ransomNote[char] = 1

        for char2 in magazine: # o(N)
            if char2 in dict_magazine:
                dict_magazine[char2] +=1
            else:
                dict_magazine[char2] = 1

        if len(dict_magazine) <1:
            return False 
        print(dict_magazine)
        print(dict_ransomNote)
        output=0
        for key, value in dict_ransomNote.items():# O(n) 
            if key in dict_magazine and value <= dict_magazine[key]:
                output+=1
            else:
                output-=1
        return output == len(dict_ransomNote)