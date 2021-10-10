class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res, index = 0, 0
        
        
        for i in range(len(nums) - 2):
            if nums[i+2] - nums[i+1] == nums[i+1] - nums[i]:
                index += 1
                res += index
            else:
                index = 0
        
        return res