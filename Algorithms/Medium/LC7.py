def reverse(x: int) -> int:
    flag = True if x > 0 else False
    neg_threshold = -2**31
    pos_threshold = 2**31 + 1
    s = str(abs(x))
    r = s[::-1]
    res = int(r)
    if (flag and res>pos_threshold) or (not flag and res*-1 < neg_threshold):
        return 0
    else:
        return res if flag else res*-1