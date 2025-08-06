class Solution:

    def encode(self, strs: list[str]) -> str:
        output = ''
        for i in strs:
            output += i + '_'
        return output
    
    def decode(self, s: str) -> list[str]:
        output = []
        string = ''
        for i in s[:]:
            if i == '_':
                output.append(string)
                string = '' 
            else:
                string += i
        return output

input= ["neet","code","love","you"]

encoded_string = Solution.encode(Solution, input)
print(Solution.decode(Solution, encoded_string))
        