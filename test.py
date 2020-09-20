import unittest
from storage import Storage

class StorageTests(unittest.TestCase):
    def test_default_first_number_when_division(self):
        storage_test_instance = Storage()
        test_case_input = "/2"
        for test_input in test_case_input:
            storage_test_instance.into_storage(test_input)
        display = storage_test_instance.show_storage()
        display_ans = storage_test_instance.show_answer()

        self.assertEqual(display, '1 / 2')
        self.assertEqual(display_ans, '0.5')

    def test_default_first_number_when_addition(self):
        storage_test_instance = Storage()
        test_case_input = "+2"
        for test_input in test_case_input:
            storage_test_instance.into_storage(test_input)
        display = storage_test_instance.show_storage()
        display_ans = storage_test_instance.show_answer()

        self.assertEqual(display, '0 + 2')
        self.assertEqual(display_ans, '2.0')

    def test_more_than_one_operator_input_consecutively(self):
        storage_test_instance = Storage()
        test_case_input = "3+-2"
        for test_input in test_case_input:
            storage_test_instance.into_storage(test_input)
        display = storage_test_instance.show_storage()
        display_ans = storage_test_instance.show_answer()

        self.assertEqual(display, '3 - 2')
        self.assertEqual(display_ans, '1.0')


    def test_clear_input_call(self):
        storage_test_instance = Storage()
        test_case_input = "3/3+2C1"
        for test_input in test_case_input:
            storage_test_instance.into_storage(test_input)
        display = storage_test_instance.show_storage()
        display_ans = storage_test_instance.show_answer()

        self.assertEqual(display, '3 / 3 + 1')
        self.assertEqual(display_ans, '2.0')

    def test_multiple_decimal_inputs_in_one_floating_number_cosiders_first_decimal(self):
        storage_test_instance = Storage()
        test_case_input = "0.5.5+1.5"
        for test_input in test_case_input:
            storage_test_instance.into_storage(test_input)
        display = storage_test_instance.show_storage()
        display_ans = storage_test_instance.show_answer()

        self.assertEqual(display, '0.55 + 1.5')
        self.assertEqual(display_ans, '2.05')

    def test_multiplicative_inverse_call(self):
        storage_test_instance = Storage()
        test_case_input = "3/2i+1"
        for test_input in test_case_input:
            storage_test_instance.into_storage(test_input)
        display = storage_test_instance.show_storage()
        display_ans = storage_test_instance.show_answer()

        self.assertEqual(display, '3 / -2.0 + 1')
        self.assertEqual(display_ans, '-0.5')

if __name__ == '__main__':
    unittest.main()
