class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1 or x==0 or x==1:
            return x
        flag = 1 if x >= 0 or not n%2 else -1
        return abs(x)**n*flag

        