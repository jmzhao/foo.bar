import unittest
import solution

class TestSolution(unittest.TestCase):
    def subject(self, *args) :
        return solution.answer(*args)

    def test_empty(self):
        self.assertEqual(self.subject([]), 0)

    def test_given_example_1(self) :
        self.assertEqual(self.subject(["foo", "bar", "oof", "bar"]), 2)

    def test_given_example_2(self) :
        self.assertEqual(self.subject(["x", "y", "xy", "yy", "", "yx"]), 5)

if __name__ == '__main__':
    unittest.main()
