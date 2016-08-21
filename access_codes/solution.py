def answer(codes):
    s = set()
    for code in codes :
        s.add(min(code, ''.join(reversed(code))))
    return len(s)
