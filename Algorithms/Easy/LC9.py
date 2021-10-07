class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            res = 0
            temp = x
            while x>0:
                res = res*10 + x%10
                x = x//10
            return res == temp