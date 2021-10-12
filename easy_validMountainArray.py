class Solution:
    def validMountainArray(self, arr):
        downHill=0
        peak=len(arr)
        if len(arr)<3:
            return False
        for i in range(len(arr)-1):
            if arr[i+1]>arr[i]:
                peak=i+1
            if arr[i]>arr[i+1]:
                downHill=i+1
                if peak>downHill:
                    print(peak, downHill)
                    return False
            if arr[i]==arr[i+1]:
                return False
        if peak>downHill:
            return False
        return True