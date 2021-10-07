class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for i in s:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        res = -1
        for i in range(len(s)):
            if count[s[i]] == 1:
                res = i
                break
        return res
        
        