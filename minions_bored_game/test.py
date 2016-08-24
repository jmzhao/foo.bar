import unittest
import solution

class TestSolution(unittest.TestCase):
    def subject(self, *args) :
        return solution.answer(*args)

    def test_given_example_1(self) :
        self.assertEqual(1,
            self.subject(1, 2))

    def test_given_example_2(self) :
        self.assertEqual(3,
            self.subject(3, 2))

    def test_largest(self) :
        self.subject(1000, 1000)

if __name__ == '__main__':
    unittest.main()
