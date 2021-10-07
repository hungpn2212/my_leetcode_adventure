class Solution:
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(1,n+1):
            if i%7!=0:
                res = res + i%7 + i//7
            else:
                res = res + i//7 + 6
        return res
        