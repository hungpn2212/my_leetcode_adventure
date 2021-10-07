class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX = 2147483647
        MIN = -2147483648
        # Check for overflow
        if divisor == 0 or (dividend == MIN and divisor == -1):
            return MAX

        flag = -1 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 1

        ans = 0

        absoluteDividend = abs(dividend)
        absoluteDivisor = abs(divisor)

        while absoluteDividend >= absoluteDivisor:
            shift = 0
            while absoluteDividend >= (absoluteDivisor << shift):
                shift += 1
            ans += (1 << (shift - 1))
            absoluteDividend -= absoluteDivisor << (shift - 1)
        return ans * flag