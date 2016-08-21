import unittest
import solution

class TestSolution(unittest.TestCase):
    def subject(self, *args) :
        return solution.answer(*args)

    def test_empty_string(self):
        self.assertEqual(self.subject(''), '')

    def test_digit(self):
        self.assertEqual(self.subject('1'), '1')

    def test_only_multiplication(self):
        self.assertEqual(self.subject('1*2*3*2*1'), '12321****')

    def test_only_addition(self):
        self.assertEqual(self.subject('1+2+3+2+1'), '12321++++')

    def test_mixed_expression(self):
        self.assertEqual(self.subject('1+2*3+2*1'), '123*21*++')

    def test_given_example_1(self) :
        self.assertEqual(self.subject("2+3*2"), "232*+")

    def test_given_example_2(self) :
        self.assertEqual(self.subject("2*4*3+9*3+5"), "243**93*5++")

if __name__ == '__main__':
    unittest.main()
