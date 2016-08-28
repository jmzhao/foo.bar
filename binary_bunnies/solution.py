def answer(seq):
    return str(n_orders(seq))

def n_orders(seq) :
    if len(seq) <= 2 : return 1
    seq_larger = [x for x in seq if x > seq[0]]
    seq_smaller = [x for x in seq if x < seq[0]]
    return n_orders(seq_larger) * n_orders(seq_smaller) * C(len(seq) - 1, len(seq_larger))

def C(n, r) :
    if r > n // 2 : r = n - r
    if r <= 0 : return 1
    res = 1
    for i in range(r) :
        res *= n - i
        res //= i + 1
    return res
