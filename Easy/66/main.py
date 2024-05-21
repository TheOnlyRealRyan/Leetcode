# Class Here
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] +=1
        for i in range(len(digits))[::-1]:
            if digits[i] == 10:
                digits[i] = 0
                if i == 0:
                    digits = [1] + digits 
                else:
                    digits[i-1]+=1
        return digits


if __name__ == "__main__":
    digits = [9]
    print(Solution.plusOne(Solution, digits))