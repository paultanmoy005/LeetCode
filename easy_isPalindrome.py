class Solution:
    def isPalindrome(self, x):
        return list(str(x)) == list(str(x))[::-1]
