from storage import Storage

def test1(storage_instance: Storage) -> tuple:
    test_case_input = "/2"
    for test_input in test_case_input:
        storage_instance.into_storage(test_input)
    display = storage_instance.show_storage()
    display_ans = storage_instance.show_answer()
    return (display,
            display_ans,
            1 if display == '1 / 2' and display_ans == '0.5' else 0
            )


def test2(storage_instance: Storage) -> tuple:
    test_case_input = "+2"
    for test_input in test_case_input:
        storage_instance.into_storage(test_input)
    display = storage_instance.show_storage()
    display_ans = storage_instance.show_answer()
    return (display,
            display_ans,
            1 if display == '0 + 2' and display_ans == '2.0' else 0
            )


def test3(storage_instance: Storage) -> tuple:
    test_case_input = "3+-2"
    for test_input in test_case_input:
        storage_instance.into_storage(test_input)
    display = storage_instance.show_storage()
    display_ans = storage_instance.show_answer()
    return (display,
            display_ans,
            1 if display == '3 - 2' and display_ans == '1.0' else 0
            )


def test4(storage_instance: Storage) -> tuple:
    test_case_input = "3/3+2C-1"
    for test_input in test_case_input:
        storage_instance.into_storage(test_input)
    display = storage_instance.show_storage()
    display_ans = storage_instance.show_answer()
    return (display,
            display_ans,
            1 if display == '3 / 3 - 1' and display_ans == '0.0' else 0
            )


def test5(storage_instance: Storage) -> tuple:
    test_case_input = "0.5.5+1.5"
    for test_input in test_case_input:
        storage_instance.into_storage(test_input)
    display = storage_instance.show_storage()
    display_ans = storage_instance.show_answer()
    return (display,
            display_ans,
            1 if display == '0.55 + 1.5' and display_ans == '2.05' else 0
            )


if __name__ == '__main__':

    for test in [test1, test2, test3, test4, test5]:
        storage_instance = Storage()
        result = test(storage_instance)
        print("{}: got {}, {}, valid? {}"
              .format(test.__name__, result[0],
                      result[1], ["no", "yes"][result[2]]))

