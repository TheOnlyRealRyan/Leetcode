def isPalindrome(x: int) -> bool:
        return str(x)[::-1] == str(x)
    
if __name__ == "__main__":
    print(isPalindrome("abcdedcba"))