import unittest

from core_logic import Calculate


class CoreLogicTests(unittest.TestCase):
    def go_for_testing(self, test_case_input: str):
        test_case_input = list(test_case_input)
        calculate_instance = Calculate(test_case_input)
        result = calculate_instance.calculate()
        return result

    def test_calculate_works(self):
        test_case_input = "1+2+3"
        result = self.go_for_testing(test_case_input)

        self.assertEqual(result, "6.0")

if __name__ == "__main__":
    unittest.main()