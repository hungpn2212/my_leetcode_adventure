class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1]]
        for i in range(1, rowIndex+1):
            left = dp[i-1] + [0]
            right = [0] + dp[i-1]
            dp.append([left[i]+right[i] for i in range(len(left))])
        return dp[-1]