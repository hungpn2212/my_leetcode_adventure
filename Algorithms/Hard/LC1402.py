class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        # Maximum result can be achieved by placing greater elements in greater index
        
        result = 0
        for index, num in enumerate(satisfaction):
            result += (index+1)*num
        #Every time you remove the first element of satisfaction, you remove the sum of the current satisfaction 
        """For example
        Example 1: sorted array: -9 -8 -1 0 5 sum = -9 + -8*2 + -1*3 + 0 + 5*5
        after you remove -9: new_array: -8 -1 0 5 new_sum = -8 + -1*2 + 0 + 5*4 = sum - (-9 + -8 + -1 + 0 + 5)
        
        """
        for i in range(n):
            temp = sum(satisfaction[i:])
            if temp < 0:
                result -= temp
            else:
                break
        return result