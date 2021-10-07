class Solution:

# I know i have to implement in O(n) time ....
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        res = 1
        for num in nums:
            if num == res:
                res += 1
        return res