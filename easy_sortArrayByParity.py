class Solution:
    def sortArrayByParity(self, nums):
        return list(filter(lambda x: x%2==0, nums)) + list(filter(lambda x: x%2==1, nums))
