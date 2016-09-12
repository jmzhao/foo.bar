import unittest
import random
import solution

class TestSolution(unittest.TestCase):
    def subject(self, *args) :
        return solution.answer(*args)

    def test_given_example_1(self) :
        self.assertEqual(2,
            self.subject([[1, 1], [0, 0]]))

    def test_given_example_2(self) :
        self.assertEqual(-1,
            self.subject([[1, 1, 1], [1, 0, 0], [1, 0, 1]]))

    def test_minimal_input(self) :
        self.assertEqual(0,
            self.subject([[0]]))
        self.assertEqual(1,
            self.subject([[1]]))

    def test_large_input(self) :
        T = 5
        n = 15
        for _ in range(T) :
            a = [[random.choice((0, 1)) for _ in range(n)] for _ in range(n)]
            self.subject(a)

if __name__ == '__main__':
    unittest.main()
