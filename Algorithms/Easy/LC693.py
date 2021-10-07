class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = ''
        while n>0:
            res = res + str(n%2)
            n = n//2
        if '11' in res or '00' in res:
            return False
        else:
            return True