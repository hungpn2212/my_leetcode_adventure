class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        mul_index = 1
        for i in reversed(num2):
            res += int(num1) * int(i) * mul_index
            mul_index *= 10
        return str(res)
            