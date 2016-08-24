P = 123454321

def answer(t, n):
    l = [0] * n
    l[0] = 1
    for _ in range(t) :
        l = [sum(t_from)%P for t_from in zip([0] + l[:-1], l, l[1:-1] + [0, 0])]
    return l[-1]
