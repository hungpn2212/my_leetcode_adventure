class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        possible = lambda s: sum(math.ceil(d / s) for d in dist[:-1]) + dist[-1] / s <= hour
        low = 0
        high = 10**7
        while low + 1 < high:
            mid = low + (high-low)// 2
            if (possible(mid)):
                high = mid
            else:
                low = mid
        return high if possible(high) else -1

