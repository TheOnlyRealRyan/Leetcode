class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        """ Find smallest word for efficiency"""
        smallestWord = 201*"a"
        for i in strs:
            if len(i) < len(smallestWord):
                smallestWord = i
        
        """ 
            loop through beginning of each word in array.
            Stop if comparison changes/does not match
        """
        if len(strs) == 1:
            return str(strs[0])
     
        comparison = ""
        newWord = ""
        """ Implement efficiency"""
        if len(smallestWord) == 1:
            loop = 1
        else:
            loop = len(smallestWord)
            
        for length in range(loop):
            for word in strs:                
                if comparison == "":                 
                    comparison += word[length]
                elif word[length] == comparison[0]:
                    comparison += word[length]               
                else:
                    return newWord
            if comparison != "":
                newWord += comparison[0]
            comparison = "" 
             
        return newWord
        
if __name__ == "__main__":
    strs = ["flower","flower","flower","flower"]
    print(Solution.longestCommonPrefix(Solution, strs))