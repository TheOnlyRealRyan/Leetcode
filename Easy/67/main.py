# Class Here
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a, base=2)+int(b, base=2))).removeprefix("0b")

        
        
if __name__ == "__main__":
    a = "11"
    b = "1"
    print(Solution.addBinary(Solution, a, b))