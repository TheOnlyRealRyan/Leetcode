# Class Here
class Solution:
    def mySqrt(self, x: int) -> int:
        # VERY slow (1.7 seconds) because time = n = 2^31 - 1
        for i in range(x):
            a = (i+1)*(i+1)
            if a == x:
                return i+1
            elif a > x:
                return i     
        return 0
    
    

if __name__ == "__main__":
    x = 1
    print(Solution.mySqrt(Solution, x))