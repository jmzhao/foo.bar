def answer(names):
    return list(sorted(names,
        key=lambda name : (score(name), name),
        reverse=True))

def score(name) :
    return sum(map(lambda c : ord(c) - ord('a') + 1, name))
