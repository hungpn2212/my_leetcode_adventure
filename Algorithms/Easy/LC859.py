class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        st = set(ch for ch in s)
        if s == goal and len(st) < len(goal):
            return True

        n = len(s)
        index_diff = []


        for i in range(n):
            if s[i] != goal[i]:
                index_diff.append(i)
            if len(index_diff) > 3:
                return False
        
        return len(index_diff) == 2 and s[index_diff[0]] == goal[index_diff[1]] and s[index_diff[1]] == goal[index_diff[0]]