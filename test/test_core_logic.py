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

    def test_trigonometric_func(self):
        test_case_input_1 = ['sin', '90']
        test_case_input_2 = ['cos', '90']
        test_case_input_3 = ['tan', '90']
        result_1 = self.go_for_testing(test_case_input_1)
        result_2 = self.go_for_testing(test_case_input_2)
        result_3 = self.go_for_testing(test_case_input_3)

        self.assertAlmostEqual(float(result_1), 0.8939966636005579, places=3)
        self.assertAlmostEqual(float(result_2), -0.4480736161291701, places=3)
        self.assertAlmostEqual(float(result_3), -1.995200412208242, places=3)

    def test_arctrigonometric_func(self):
        test_case_input_1 = ['asin', '0.89']
        test_case_input_2 = ['acos', '-0.44']
        test_case_input_3 = ['atan', '-1.99']
        result_1 = self.go_for_testing(test_case_input_1)
        result_2 = self.go_for_testing(test_case_input_2)
        result_3 = self.go_for_testing(test_case_input_3)

        self.assertAlmostEqual(float(result_1), 1.0973451695228305, places=3)
        self.assertAlmostEqual(float(result_2), 2.02639500019072, places=3)
        self.assertAlmostEqual(float(result_3), -1.1051406883644943, places=3)

    def test_factorial(self):
        test_case_input = ['3', '!']
        result = self.go_for_testing(test_case_input)

        self.assertEqual(result, "6")

    def test_log_and_naturalLog(self):
        test_case_input_1 = ['log', '20']
        test_case_input_2 = ['ln', '20']
        result_1 = self.go_for_testing(test_case_input_1)
        result_2 = self.go_for_testing(test_case_input_2)

        self.assertAlmostEqual(float(result_1), 1.301029995663981, places=3)
        self.assertAlmostEqual(float(result_2), 2.995732273553991, places=3)

    def test_unary_operator(self):
        test_case_input = ['log', '10', '+', '3']
        result = self.go_for_testing(test_case_input)

        self.assertEqual(result, "4.0")


if __name__ == "__main__":
    unittest.main()
