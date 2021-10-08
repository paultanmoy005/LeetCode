class Solution:
    def twoSum(self, nums, target):
        for n1 in nums:
            n2 = target - n1
            if n2 in nums:
                idx = [i for i, x in enumerate(nums) if x == n2]
                if nums.index(n1) in idx:
                    idx.remove(nums.index(n1))
                if len(idx)>0:
                    return [nums.index(n1),idx[0]]