import unittest
import random
import solution

class TestSolution(unittest.TestCase):
    def subject(self, *args) :
        return solution.answer(*args)

    def test_given_example_1(self) :
        self.assertEqual(-1,
            self.subject([[2, 1], [2, 0], [3, 1], [1, 0]]))

    def test_given_example_2(self) :
        self.assertEqual(1,
            self.subject([[1, 2], [1, 1], [2, 2]]))

    def test_minimal_input(self) :
        self.assertEqual(-1,
            self.subject([[0]]))

    def test_impossible(self) :
        self.assertEqual(-2,
            self.subject(zip(*[[0, 1, 2], [2, 1, 0], [1, 0, 2]])))

    def test_an_arbitary_case(self) :
        self.assertEqual(-1,
            self.subject(zip(*[[1, 2, 0, 4, 5, 6, 3], [1, 1, 1, 1, 5, 6, 4]])))
        self.assertEqual(-1,
            self.subject(zip(*reversed([[1, 2, 0, 4, 5, 6, 3], [1, 1, 1, 1, 5, 6, 4]]))))

    def test_big_input(self) :
        n_stops = 50
        n_dirs = 10
        all_stops = list(range(n_stops))
        self.subject([[random.choice(all_stops) for _ in range(n_dirs)] for _ in range(n_stops)])

if __name__ == '__main__':
    unittest.main()
