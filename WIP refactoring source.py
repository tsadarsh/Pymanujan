# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
from tkinter import Tk
from tkinter import ttk
from tkinter import StringVar
from collections import OrderedDict


class Storage:
    __operators: list = ['/', '*', '+', '-']
    __special: list = ['C', 'AC', 'P/M']
    __storage: list
    __result: str

    def __init__(self):
        self.__storage = []

    def show_answer(self, other=None):
        other.set(self.__answer)
        return self.__answer

    def go_for_calc(self):
        obj = Calculate(self.__storage, self.__operators.copy())
        self.__answer = obj.calculate()

    def show_storage(self, other=None) -> str:
        this = ''.join(
                       map(
                           lambda i: ' '+i+' ' if i in self.__operators else i,
                           self.__storage)
                           )
        other.set(this)
        return this

    def show_storage_as_list(self) -> list:
        return self.__storage

    def into_storage(self, character) -> None:
        print(character)
        ''' Logic to add input to storage '''
        if character in self.__operators:
            return self.__put_operator(character)
        if character in self.__special:
            return self.__apply_special(character)
        if character is '.':
            return self.__put_dot(character)
        if not character.isnumeric() and character != '.':
            raise ValueError
        return self.__put_digit(character)

    def __put_operator(self, operator) -> None:
        if len(self.__storage) > 0:
            ''' Not first input '''
            if self.__storage[-1] in self.__operators:
                ''' Changing 3+- to 3- '''
                self.__storage[-1] = operator
            else:
                ''' DEFAULT: Adding operator '''
                self.__storage.append(operator)
        else:
            ''' First entry to __storage '''
            self.__storage.extend([['1', '0']
                                  [self.__operators.index(operator)//2],
                                   operator])

    def __apply_special(self, special) -> None:
        if special == 'AC':
            self.__storage.clear()
        if special == 'C':
            self.__storage.pop(-1)
        if special == 'P/M':
            ''' Multiplicative inverse of last number chunk.
            Diabled when last input is operator '''
            self.__storage[-1] *= -1

    def __put_digit(self, digit) -> None:
        if len(self.__storage) == 0 or self.__storage[-1] in self.__operators:
            ''' First entry or previous chunk is operator '''
            self.__storage.append(digit)
        else:
            ''' Appending continuing digits '''
            self.__storage[-1] += digit

    def __put_dot(self, dot):
        if len(self.__storage) == 0:
            self.__storage.append("0.")
            return
        if ((self.__storage[-1] not in self.__operators) and
           (dot not in self.__storage[-1])):
            self.__storage[-1] += dot


class Calculate():
    ans: str
    _get_value = {
            '/': lambda x, y: x/y,
            '*': lambda x, y: x*y,
            '+': lambda x, y: x+y,
            '-': lambda x, y: x-y
            }

    def __init__(self, expr_as_list, operators):
        self.expr_as_list = expr_as_list
        self.operators = operators

    def calculate(self) -> str:
        while self.operators[0] in self.expr_as_list:
            index = self.expr_as_list.index(self.operators[0])
            self.__partial_calculate(index)
        while self.operators[1] in self.expr_as_list:
            index = self.expr_as_list.index(self.operators[1])
            self.__partial_calculate(index)
        while self.operators[2] in self.expr_as_list:
            index = self.expr_as_list.index(self.operators[2])
            self.__partial_calculate(index)
        while self.operators[3] in self.expr_as_list:
            index = self.expr_as_list.index(self.operators[3])
            self.__partial_calculate(index)
        self.ans = self.expr_as_list[0]
        return self.ans

    def __partial_calculate(self, index) -> None:
        operator = self.expr_as_list[index]
        left_operand = float(self.expr_as_list[index-1])
        right_operand = float(self.expr_as_list[index+1])
        sub_result = self._get_value[operator](left_operand, right_operand)
        self.expr_as_list[index-1:index+2] = [str(sub_result)]


class GUI:
    __layout = ['*', '/', 'C', 'AC',
                '9', '8', '7', '-',
                '6', '5', '4', '+',
                '3', '2', '1', '+/-',
                '.', '0', '=']
    __dic_layout = OrderedDict(
            {'mul': '*', 'div': '/', 'clr': 'C', 'acr': 'AC',
                'nin': '9', 'eig': '8', 'sev': '7', 'min': '-',
                'six': '6', 'fiv': '5', 'fou': '4', 'plu': '+',
                'thr': '3', 'two': '2', 'one': '1', 'pam': '+/-',
                'dot': '.', 'zer': '0', 'equ': '='}
            )
    bt_cmd = Storage()

    root = Tk()
    root.title("PyCalc v0.1-beta")
    root.resizable(False, False)

    styler = ttk.Style()
    styler.theme_use("clam")
    styler.configure("TButton", width='5', padding='10')
    styler.configure("TLabel", font='Helvetica 24')
    DISPLAY = StringVar()
    DISPLAY.set(' ')

    def startapp(self):
        content = ttk.Frame(master=self.root, padding=(3, 3, 3, 3))
        mainframe = ttk.Frame(master=content, relief='sunken')

        display = ttk.Frame(master=content, relief='flat')
        display['borderwidth'] = 10
        val_display = ttk.Label(master=display, textvariable=self.DISPLAY)

        keypad = ttk.Frame(master=mainframe)

        ''' Control Binding '''
        buttons = []
        for bt_text in self.__layout[:-1]:
            bt = ttk.Button(master=keypad)
            bt['text'] = bt_text
            bt['command'] = lambda: (self.bt_cmd.into_storage(bt_text),
                                     self.bt_cmd.show_storage(self.DISPLAY))
            buttons.append(bt)
        ''' Control binding for '='. '''
        bt_equal = ttk.Button(master=keypad)
        bt_equal['text'] = self.__layout[-1]
        bt_equal['command'] = lambda: (self.bt_cmd.go_for_calc(),
                                       self.bt_cmd.show_answer(self.DISPLAY))
        buttons.append(bt_equal)

        ''' Gridding '''
        content.grid(row=0, column=0)
        mainframe.grid(row=0, column=0)
        display.grid(row=0, column=0, columnspan=4, pady=5, padx=5)
        val_display.grid(row=0, column=0, columnspan=4)
        keypad.grid(row=1, column=0, rowspan=5, columnspan=4)
        for b_index in range(len(buttons)-1):
            buttons[b_index].grid(row=(b_index//4)+1, column=b_index % 4)
        ''' Gridding for '='. '''
        buttons[-1].grid(row=5, column=2, columnspan=2)

        self.root.mainloop()


def test0(gui_instance: GUI):
    gui_instance.startapp()


def test1(storage_instance: Storage) -> tuple:
    test_case_input = "/2"
    for test_input in test_case_input:
        storage_instance.into_storage(test_input)
    display = storage_instance.show_storage()
    storage_instance.go_for_calc()
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
    storage_instance.go_for_calc()
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
    storage_instance.go_for_calc()
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
    storage_instance.go_for_calc()
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
    storage_instance.go_for_calc()
    display_ans = storage_instance.show_answer()
    return (display,
            display_ans,
            1 if display == '0.55 + 1.5' and display_ans == '2.05' else 0
            )


if __name__ == '__main__':
    gui_instance = GUI()
    test0(gui_instance)
'''
    for test in [test1, test2, test3, test4, test5]:
        storage_instance = Storage()
        result = test(storage_instance)
        print("{}: got {}, {}, valid? {}"
              .format(test.__name__, result[0],
                      result[1], ["no", "yes"][result[2]]))
'''

