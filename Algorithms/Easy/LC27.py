class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for x in nums[:]:
            if x == val:
                nums.remove(x)
        
     
        return len(nums)