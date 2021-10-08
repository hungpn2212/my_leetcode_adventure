class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                if i == len(nums) - 2:
                    return nums[i+1]
                elif i == 0:
                    return nums[i]
                else:
                    if nums[i] != nums[i-1]:
                        return nums[i]
                    else:
                        continue
                