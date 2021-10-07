class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, start = 0, 0
        dict = {}
        for i in range(len(s)):
            if s[i] not in dict or dict[s[i]] < start:
                res = max(res, i-start+1)
            else:
                start = dict[s[i]] + 1
            dict[s[i]] = i
        return res