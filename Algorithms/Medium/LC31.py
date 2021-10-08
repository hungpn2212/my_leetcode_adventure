# I dont really understand permutations, until today
# Great article that explained everything: https://www.nayuki.io/res/next-lexicographical-permutation-algorithm/next-permutation-algorithm.svg
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        # Find the longest decrease suffix
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
            
        # i = 0 means that the array already in decreasing form, then just reverse it
        if i == 0:
            nums.reverse()
            return
        # The pivot
        pivot = i - 1
        j = len(nums) - 1
        while nums[j] <= nums[pivot]:
            j -= 1
        nums[pivot], nums[j] = nums[j], nums[pivot]
        
        #Reverse the suffix part
        
        left, right = pivot + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        