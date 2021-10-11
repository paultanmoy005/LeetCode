class Solution:
    def checkIfExist(self, arr):
        if arr.count(0)>1:
            return True
        for i in arr:
            if i is not 0 and (i*2 in arr or i/2 in arr):
                return True
        return False