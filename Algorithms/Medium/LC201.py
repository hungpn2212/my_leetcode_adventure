class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left != right:
            right >>= 1
            left >>= 1
            i += 1
        return right << i