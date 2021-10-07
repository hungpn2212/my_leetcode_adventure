class Solution:
    def jump(self, nums: List[int]) -> int:
        l, curr, nxt, ans, index = len(nums) - 1, -1, 0, 0, 0
        while nxt < l:
            if index > curr:
                ans += 1
                curr = nxt
            nxt = max(nxt, nums[index] + index)
            index += 1
        return ans