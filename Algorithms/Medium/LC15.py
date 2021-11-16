class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = set()
        for k in range(n):
            two_sum = -nums[k]
            i, j = k+1, n-1
            while i < j:
                if nums[i]+nums[j] > two_sum:
                    j -= 1
                elif nums[i] + nums[j] < two_sum:
                    i += 1
                else:
                    ans.add((nums[k], nums[i], nums[j]))
                    i += 1
                    j -= 1
        return ans