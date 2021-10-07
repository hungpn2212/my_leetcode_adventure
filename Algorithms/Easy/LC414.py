def thirdMax(nums: List[int]) -> int:
    l = list(set(nums))
    l.sort()
    if len(l) < 3:
        return max(l)
    else:
        return l[-3]