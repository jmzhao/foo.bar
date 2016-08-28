import unittest
import solution

class TestSolution(unittest.TestCase):
    def subject(self, *args) :
        return solution.answer(*args)

    def test_given_example_1(self) :
        self.assertEqual("4",
            self.subject("7"))

    def test_given_example_2(self) :
        self.assertEqual("None",
            self.subject("100"))

    def test_small_number(self) :
        self.assertEqual("1",
            self.subject("1"))
        self.assertEqual("2",
            self.subject("2"))

    def test_first_1000(self) :
        l = [f(n) for n in range(1000)]
        for i in range(3, 1000) :
            pos = find_last(l, i)
            self.assertEqual(str(pos),
                self.subject(i))

    def test_big_number(self) :
        self.subject("1234567890123456789012345")

def find_last(l, x, start=1) :
    try :
        pos = l.index(x, start)
    except ValueError :
        return None
    while True :
        try :
            npos = l.index(x, pos + 1)
            pos = npos
        except ValueError :
            return pos

def cached(f) :
    cache = dict()
    def decorated(*args) :
        return cache.setdefault(args, f(*args))
    return decorated

@cached
def f(nn) :
    if nn > 2 :
        n = nn // 2
        if nn % 2 == 0 :
            return f(n) + f(n+1) + n
        else :
            return f(n-1) + f(n) + 1
    elif nn == 2 :
        return 2
    else :
        return 1

if __name__ == '__main__':
    unittest.main()
