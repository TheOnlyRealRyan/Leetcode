class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        open_bracket ='({['
        for i in s:
            if i in open_bracket:
                stack.append(i)
            else:
                if len(stack) == 0 or i == ')' and stack.pop() != '(' or i == '}' and stack.pop() != '{' or i == ']' and stack.pop() != '[':
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    s = "]"
    print(Solution.isValid(Solution, s))