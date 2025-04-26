def max_steal(val,i=0):
    n = len(val)
    if i >= n:
        return 0
    p = val[i] + max_steal(val, i+2)
    s = max_steal(val, i+1)
    return max(p,s)
val = [6, 7, 1, 3, 8, 2, 5]
print(max_steal(val))
