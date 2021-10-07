class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        def same_line(point1: List[int], point2: List[int], point3: List[int]) -> int:
                return (point2[0] - point1[0]) * (point3[1]-point1[1]) == (point3[0] - point1[0]) * (point2[1] - point1[1])
            
        
        if n <= 2:
            return n
        else:
            res = 2
            
            for i in range(n-2):
                for j in range(i+1, n-1):
                    c = 2
                    for k in range(j+1, n):
                        if same_line(points[i], points[j], points[k]):
                            c+=1
                    res = max(res, c)
            return res
            
            
        
        