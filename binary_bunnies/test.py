import unittest
import solution

class TestSolution(unittest.TestCase):
    def subject(self, *args) :
        return solution.answer(*args)

    def test_given_example_1(self) :
        self.assertEqual("6",
            self.subject([5, 9, 8, 2, 1]))

    def test_given_example_2(self) :
        self.assertEqual("1",
            self.subject([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    def test_empty(self) :
        self.assertEqual("1",
            self.subject([]))

    def test_big_input(self) :
        import random
        for _ in range(5) :
            l = list(range(50))
            random.shuffle(l)
            self.subject(l)

if __name__ == '__main__':
    unittest.main()
