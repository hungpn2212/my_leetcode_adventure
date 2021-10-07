def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    hash_set = set()
    
    for i in range(len(nums)):

        if nums[i] in hash_set: 
            return True
        hash_set.add(nums[i])

        # Remove the element a[j] which i - j > k
        if len(hash_set) > k:
            hash_set.remove(nums[i - k])
    return False