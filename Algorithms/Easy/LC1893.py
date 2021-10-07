def isCovered(ranges, left, right):
    base = []
    for r in ranges:
        for i in range(r[0], r[1]+1):
            base.append(i)
    b = [i for i in range(left, right+1)]
    return all(elem in base for elem in b)
