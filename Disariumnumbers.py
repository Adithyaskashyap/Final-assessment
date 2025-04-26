def is_disarium(n):
    return n == sum(int(d)**i for i, d in enumerate(str(n), 1))
def first_n_disarium(n):
    res, num = [], 0
    while len(res) < n:
        if is_disarium(num):
            res.append(num)
        num += 1
    return res
def disarium_between(a, b):
    return [x for x in range(a, b+1) if is_disarium(x)]
n = 10
print(f"First {n} Disarium numbers:\n{first_n_disarium(n)}")
a, b = 1, 200
print(f"\nDisarium numbers between {a} and {b}:\n{disarium_between(a, b)}")
