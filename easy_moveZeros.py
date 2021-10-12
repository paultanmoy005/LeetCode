class Solution:
    def moveZeroes(self, nums):
        Len=len(nums)
        for i in range(Len-2,-1,-1):
            if nums[i]==0 and nums[i+1] is not 0:
                for j in range(i+1,Len):
                    nums[j-1]=nums[j]
                nums[len(nums)-1]=0