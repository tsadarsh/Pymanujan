import unittest

from core_logic import Calculate


class CoreLogicTests(unittest.TestCase):
    def go_for_testing(self, test_case_input: list):
        calculate_instance = Calculate(test_case_input)
        result = calculate_instance.calculate()
        return result

    def test_calculate_works(self):
        test_case_input = ['1', '+', '3']
        result = self.go_for_testing(test_case_input)

        self.assertEqual(result, "4.0")

    def test_left_paren_as_first_input(self):
        test_case_input = ['(', '12', ')']
        result = self.go_for_testing(test_case_input)

        self.assertEqual(result, "12")

    def test_parenthesis_precedence(self):
        test_case_input = ['(', '3', '+', '2', ')', '*', '2']
        result = self.go_for_testing(test_case_input)

        self.assertEqual(result, "10.0")

    def test_parenthesis_precedence_2(self):
        test_case_input = ['6', '/', '(', '4', '+', '2', ')']
        result = self.go_for_testing(test_case_input)

        self.assertEqual(result, "1.0")

    def test_bracket_balencer(self):
        test_case_input = ['(', '3', '*', '(', '4', '+', '1']
        result = self.go_for_testing(test_case_input)

        self.assertEqual(result, "15.0")

    def test_bodmas(self):
        test_case_input = ['44', '-', '3', '/', '6', '+', '2', '*', '2']
        result = self.go_for_testing(test_case_input)

        self.assertEqual(result, "47.5")

if __name__ == "__main__":
    unittest.main()
