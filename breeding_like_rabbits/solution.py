def answer(str_S):
    mi = None
    s = int(str_S)
    if s <= 2 :
        mi = 2 if s == 2 else 1
    pos_even = last_appearance(s, EVEN_POSITIONS)
    pos_odd = last_appearance(s, ODD_POSITIONS)
    pos = max(pos_even if pos_even else -1, pos_odd if pos_odd else -1)
    mi = pos if pos >= 0 else None
    return str(mi)

EVEN_POSITIONS = lambda x : 2 * x
ODD_POSITIONS = lambda x : 2 * x + 1
def last_appearance(s, pos_trans) :
    lpos, rpos = 0, s
    while lpos < rpos :
        ## narraw n, where f(n) == s, within [lpos, rpos)
        mid = (lpos + rpos) // 2
        pos = pos_trans(mid)
        v = f(pos)
        if v > s :
            rpos = mid
        elif v < s :
            lpos = mid + 1
        else :
            return pos
    return None

def f(nn) :
    if nn > 2 :
        n = nn // 2
        if nn % 2 == 0 :
            return f2(n) + n
        else :
            return f2(n-1) + 1
    elif nn == 2 :
        return 2
    else :
        return 1

def f2(nn) :
    if nn > 2 :
        n = nn // 2
        if nn % 2 == 0 :
            return 2*f2(n-1) + df2(n-1) + n + 1
        else :
            return 2*f2(n-1) + df2(n-1) + df2(n) + n + 2
    else :
        return f(nn) + f(nn+1)

def df2(nn) :
    if nn > 2 :
        n = nn // 2
        if nn % 2 == 0 :
            return df2(n) + 1
        else :
            return df2(n-1)
    else :
        return f(nn+2) - f(nn)
