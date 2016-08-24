import unittest
import solution

class TestSolution(unittest.TestCase):
    def subject(self, *args) :
        return solution.answer(*args)

    def test_given_example_1(self) :
        self.assertEqual(self.subject(19, 19, 3), "03/19/19")

    def test_given_example_2(self) :
        self.assertEqual(self.subject(2, 30, 3), "Ambiguous")

    def test_invalid(self) :
        self.assertEqual(self.subject(19, 19, 19), "Invalid")

    def test_valid_when_all_same(self) :
        self.assertEqual(self.subject(3, 3, 3), "03/03/03")

if __name__ == '__main__':
    unittest.main()
