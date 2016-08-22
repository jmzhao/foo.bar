import unittest
import solution

class TestSolution(unittest.TestCase):
    def subject(self, *args) :
        return solution.answer(*args)

    def test_empty(self):
    # Inputs:
        food = 7
        grid = [[0]]
    # Output:
        ans = 7
        self.assertEqual(self.subject(food, grid), ans)

    def test_given_example_1(self) :
    # Inputs:
        food = 7
        grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
    # Output:
        ans = 0
        self.assertEqual(self.subject(food, grid), ans)

    def test_given_example_2(self) :
    # Inputs:
        food = 12
        grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
    # Output:
        ans = 1
        self.assertEqual(self.subject(food, grid), ans)

    def test_minimal(self) :
    # Inputs:
        food = 4
        grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
    # Output:
        ans = 0
        self.assertEqual(self.subject(food, grid), ans)

    def test_impossible(self) :
    # Inputs:
        food = 3
        grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
    # Output:
        ans = -1
        self.assertEqual(self.subject(food, grid), ans)

if __name__ == '__main__':
    unittest.main()
