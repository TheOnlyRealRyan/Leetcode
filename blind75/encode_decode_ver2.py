class Solution:

    def encode(self, strs: list[str]) -> str:
        output = ''
        output+=str(len(strs))
        for i in strs:
            output += str(len(i))
        for i in strs:
            output += i
        return output
    
    
    def decode(self, s: str) -> list[str]:
        output = []
        string = ''
        length = int(s[0]) # find length of original arr
        s = s[1::] # remove first char
        
        for i, x in enumerate(s[:length]):
            string =  s[length:length+int(x):]
            s = s[:length:] + s[length+length::]
            output.append(string)
        return output
    
input= ["neet","code","love","you"]

encoded_string = Solution.encode(Solution, input)
print(Solution.decode(Solution, encoded_string))
        