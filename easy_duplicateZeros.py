class Solution:
    def duplicateZeros(self, arr):
        idx0 = [i for i, j in enumerate(arr) if j == 0]
        print(idx0)
        shift = 0
        for i in idx0:
            arr.insert(i+ shift+ 1, 0)
            arr.pop()
            shift = shift + 1