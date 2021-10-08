# Copy the idea of LC5

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        
        
        def validParentheses(s) -> bool:
            stack = []
            for i in s:
                if i == "(":
                    stack.append(i)
                else:
                    if len(stack) > 0:
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0
            
        if validParentheses(s):
            return len(s)
        start = len(s) - 1
        while start > 1:
            for i in range(0, len(s) - start+1):
                if validParentheses(s[i:i+start]):
                    return start
            start -= 1
        return 0