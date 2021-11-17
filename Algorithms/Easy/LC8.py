class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        negative = False
        first_charecter = True
        for i in range(len(s)):
            if ord(s[i]) == 32 and first_charecter:
                pass
            elif ord(s[i]) == 45 or ord(s[i]) == 43:
                if not first_charecter:
                    break
                elif ord(s[i]) == 45:
                    negative = True
                    first_charecter = False
                elif ord(s[i])==43 and first_charecter == True:
                    first_charecter = False
            elif ord(s[i]) > 58 or ord(s[i]) < 47:
                break
            else:
                result = result*10 + int(s[i])
                first_charecter = False
        if negative == True:
            result = result*-1
        return max(-2**31, min(result, 2**31 - 1))