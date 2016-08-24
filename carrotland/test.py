import unittest
import solution

class TestSolution(unittest.TestCase):
    def subject(self, *args) :
        return solution.answer(*args)

    def test_given_example_0(self) :
        self.assertEqual(1,
            self.subject([[-1, -1], [0, 1], [1, 0]]))

    def test_given_example_1(self) :
        self.assertEqual(289,
            self.subject([[2, 3], [6, 9], [10, 160]]))

    def test_given_example_2(self) :
        self.assertEqual(1730960165,
            self.subject([[91207, 89566], [-88690, -83026], [67100, 47194]]))

if __name__ == '__main__':
    unittest.main()
