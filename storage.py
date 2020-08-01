from core_logic import Calculate
from pyperclip import copy as to_clipboard


class Storage:
    __operators: list = ['/', '*', '+', '-']
    __special: list = ['C', 'AC', 'P/M']
    __storage: list
    __result: str

    def __init__(self):
        self.__storage = []

    def copy_to_clipboard(self):
        to_clipboard("".join(self.__storage))

    def show_answer(self):
        self.go_for_calc()
        return self.__answer

    def go_for_calc(self):
        obj = Calculate(self.__storage, self.__operators.copy())
        self.__answer = obj.calculate()

    def show_storage(self) -> str:
        this = ''.join(
                       map(
                           lambda i: ' '+i+' ' if i in self.__operators else i,
                           self.__storage)
                           )
        return this

    def show_storage_as_list(self) -> list:
        return self.__storage

    def into_storage(self, character) -> None:
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
