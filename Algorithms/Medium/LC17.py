class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0: return []
        m = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }
        result = []
        raw_input = []
        for i in digits:
            raw_input.append(m[int(i)])
        tempResut =  list (itertools.product(*raw_input))
        for i in tempResut:
            result.append("".join(i))
        return result