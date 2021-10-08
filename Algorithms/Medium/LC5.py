class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        def isPalindrome(s) -> bool:
            return s == s[::-1]
        
        if isPalindrome(s):
            return s
        start = len(s) - 1
        while start > 1:
            for i in range(0, len(s) - start+1):
                if isPalindrome(s[i:i+start]):
                    return s[i:i+start]
            start -= 1
        return s[0]