class Solution:
    def isPalindrome(self, x: int) -> bool:
        #It is never a palindrome
        if x < 0:
            return False

        s = str(x)
        return s == s[::-1]
        