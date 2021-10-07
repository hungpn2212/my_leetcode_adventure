class Solution(object):
    def numJewelsInStones(self, J, S):
        return sum(x in J for x in S)
        