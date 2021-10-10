class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = -10e7
        left = 0
        for i in range(len(values)):
            res = max(res, left+values[i]-i)
            left = max(left,values[i]+i)
        return res