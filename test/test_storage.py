import unittest

from Pymanujan.storage import Storage


class StorageTests(unittest.TestCase):
    def go_for_testing(self, test_case_input):
        storage_test_instance = Storage()
        for test_input in test_case_input:
            storage_test_instance.into_storage(test_input)
        display = storage_test_instance.show_storage()
        return display

    def test_default_first_number_when_division(self):
        test_case_input = "/2"
        display = self.go_for_testing(test_case_input)

        self.assertEqual(display, "1 / 2")

    def test_default_first_number_when_addition(self):
        test_case_input = "+2"
        display = self.go_for_testing(test_case_input)

        self.assertEqual(display, "0 + 2")

    def test_more_than_one_operator_input_consecutively(self):
        test_case_input = "3+-2"
        display = self.go_for_testing(test_case_input)

        self.assertEqual(display, "3 - 2")

    def test_clear_input_call(self):
        test_case_input = "3/3+2C1"
        display = self.go_for_testing(test_case_input)

        self.assertEqual(display, "3 / 3 + 1")

    def test_all_clear_input_call(self):
        test_case_input = "3/3+2A"
        display = self.go_for_testing(test_case_input)

        self.assertEqual(display, "")

    def test_multiple_decimal_inputs_considers_first_decimal(self):
        test_case_input = "0.5.5+1.5"
        display = self.go_for_testing(test_case_input)

        self.assertEqual(display, "0.55 + 1.5")

    def test_multiplicative_inverse_call(self):
        test_case_input = "3/2i+1"
        display = self.go_for_testing(test_case_input)

        self.assertEqual(display, '3 / -2.0 + 1')

    def test_parenthesis_working(self):
        test_case_input = "(3+2)*2"
        display = self.go_for_testing(test_case_input)

        self.assertEqual(display, "(3 + 2) * 2")

        test_case_input = "8*(3+2)/2"
        display = self.go_for_testing(test_case_input)

        self.assertEqual(display, "8 * (3 + 2) / 2")

    def test_right_paren_less_than_left_paren(self):
        test_case_input = "(3+2))*4"
        display = self.go_for_testing(test_case_input)

        self.assertEqual(display, "(3 + 2) * 4")

    def test_auto_mul_operator_before_left_parenthesis(self):
        test_case_input = "4(3+1)"
        display = self.go_for_testing(test_case_input)

        self.assertEqual(display, "4 * (3 + 1)")

    def test_const_substitution(self):
        test_case_input = "e"
        display = self.go_for_testing(test_case_input)

        self.assertEqual(display, "2.71828")

        test_case_input = "\u03C0"
        display = self.go_for_testing(test_case_input)

        self.assertEqual(display, "3.14159")

    def test_implicit_mul_operator_before_constant(self):
        test_case_input = "2\u03C0e"
        display = self.go_for_testing(test_case_input)

        self.assertEqual(display, "2 * 3.14159 * 2.71828")

    def test_correct_spacing_for_str_repr(self):
        test_case_input = ['sin', '3', '0', '+', '4', '(', 'ln', 'e']
        display = self.go_for_testing(test_case_input)

        self.assertEqual(display, "sin 30 + 4 * (ln 2.71828")

    def test_auto_nesting_of_unary_operators(self):
        test_case_input = ['log', 'sin', '3', '0']
        display = self.go_for_testing(test_case_input)

        self.assertEqual(display, "log  * (sin 30")

    def test_factorial_input(self):
        test_case_input = "3!-4"
        display = self.go_for_testing(test_case_input)

        self.assertEqual(display, "3!  - 4")


if __name__ == '__main__':
    unittest.main()
