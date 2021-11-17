class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {')':'(','}':'{',']':'['}
        for char in s:
            if char in ["(","{","["]:
                st.append(char)
            else:
                val = st.pop() if st else None
                if val != d[char]:return False
        
        if len(st) == 0 :
            return True