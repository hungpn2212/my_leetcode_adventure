class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        bucket = [[] for _ in range(len(nums)+1)]
        for key, val in d.items():
            bucket[val].append(key)

        res = []
        for row in reversed(bucket):
            if not row:
                continue
            else:
                for i in range(len(row)):
                    res.append(row[i])
                    if len(res) == k:
                        return res
            