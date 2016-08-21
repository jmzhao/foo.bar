import unittest
import solution

class TestSolution(unittest.TestCase):
    def subject(self, *args) :
        return solution.answer(*args)

    def test_empty(self):
        self.assertEqual(self.subject([]), [])

    def test_given_example_1(self) :
        self.assertEqual(self.subject(["annie", "bonnie", "liz"]), ["bonnie", "liz", "annie"])

    def test_given_example_2(self) :
        self.assertEqual(self.subject(["abcdefg", "vi"]), ["vi", "abcdefg"])

if __name__ == '__main__':
    unittest.main()
