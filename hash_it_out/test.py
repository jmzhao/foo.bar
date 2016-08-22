import unittest
import solution

class TestSolution(unittest.TestCase):
    def subject(self, *args) :
        return solution.answer(*args)

    def test_empty(self):
        self.assertEqual(self.subject([]), [])

    def test_given_example_1(self) :
        self.assertEqual(
            self.subject([0, 129, 3, 129, 7, 129, 3, 129, 15, 129, 3, 129, 7, 129, 3, 129]),
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_given_example_2(self) :
        self.assertEqual(
            self.subject([0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165]),
            [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225])

if __name__ == '__main__':
    unittest.main()
