class Solution:
    def findNumbers(self, nums):
        count = 0
        for i in nums:
            Len = len(str(i))
            if Len % 2 == 0:
                count = count + 1
        return count