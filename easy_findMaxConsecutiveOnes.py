class Solution:
    def findMaxConsecutiveOnes(self, nums):
        countOld = 0
        countNew = 0
        for i in nums:
            if i == 1:
                countNew = countNew + 1
            elif i == 0:
                countNew = 0
            if countNew > countOld:
                countOld = countNew
        return countOld