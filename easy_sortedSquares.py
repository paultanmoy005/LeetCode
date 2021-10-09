class Solution:
    def sortedSquares(self, nums):
        squares = [i**2 for i in nums]
        squares.sort()
        return squares