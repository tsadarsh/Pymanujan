from operator import neg


class Storage:
    """Class to store and retrieve inputs provided as strings

    Methods
    -------
    show_storage: str
        Returns stored characters as a single formatted string
    show_storage_as_list: list
        Returns stored characters as a list
    into_storage: None
        Stores argument `character` if logic is met
    """

    __unary_operators: list = ['sin', 'cos', 'tan', 'asin', 'acos',
                               'atan', '!', 'log', 'ln']
    __binary_operators: list = ['^', '/', '*', '+', '-']
    __dot = ['.']
    __left_paren, __right_paren = '(', ')'
    __operators: list = ['^', '/', '*', '+', '-', 'sin', 'cos', 'tan',
                         'asin', 'acos', 'atan', '!', 'log', 'ln']
    __special: list = ['C', 'A', 'i']
    __const: list = {'e': '2.71828', '\u03C0': '3.14159'}
    __storage: list
    __result: str

    def __init__(self):
        self.__storage = []

    def show_storage(self) -> str:
        """Returns stored characters as a single formatted string.

        Elements from a list containing stored characters are combined to a
        single string with whitespace around operators.
        """

        output = ''
        for ind, char in enumerate(self.__storage, start=1):
            if char in self.__binary_operators:
                output += ' '+char+' '
            elif char in self.__unary_operators:
                output += char+' '
            else:
                output += char
        return output

    def show_storage_as_list(self) -> list:
        """Returns stored characters as a list"""

        return self.__storage

    def into_storage(self, character: str) -> None:
        """Stores argument `character` if logic is met.

        Checks if `character` is unary-operator, binary-operator, special, dot,
        parenthesis, and stores in necessary format by calling corresponding
        method; `put_unary_operator` for `unary_operator` type, `put_special`
        for `special` and so on. (see reference)

        Reference
        ---------
            TYPE OF CHARACTER | METHOD CALLED
            -----------------   -------------------
            unary_operator    | put_unary_operator
            binary_operator   | put_binary_operator
            special           | apply_special
            const             | put_const
            dot               | put_dot
            left_paren        | put_left_paren
            right_paren       | put_right_paren
            .isnumeric()      | put_digit

        Arguments
        ---------
        character : str
            Character to be stored
        """

        if character in self.__unary_operators:
            return self.__put_unary_operator(character)
        elif character in self.__binary_operators:
            return self.__put_binary_operator(character)
        elif character in self.__special:
            return self.__apply_special(character)
        elif character in self.__const:
            return self.__put_const(character)
        elif character in self.__dot:
            return self.__put_dot(character)
        elif character in self.__left_paren:
            return self.__put_left_paren()
        elif character in self.__right_paren:
            return self.__put_right_paren()
        elif character.isnumeric():
            return self.__put_digit(character)
        else:
            raise ValueError

    def is_not_digit(self, item: str):
        try:
            float(item)
            return False
        except ValueError:
            return True

    def __put_unary_operator(self, character) -> None:
        if len(self.__storage) == 0:
            self.__storage.append(character)
        elif not self.is_not_digit(self.__storage[-1]):
            if character == '!':
                self.__storage.append(character)
            else:
                self.__storage.extend(['*', character])
        elif self.__storage[-1] in self.__unary_operators:
            if character == '!':
                self.__storage.extend(['*', '(', '1', character])
            self.__storage.extend(['*', '(', character])
        else:
            self.__storage.append(character)

    def __put_binary_operator(self, character) -> None:
        """Logic for characters of type operator before storing

        In case storage is empty, if operator is addive, `0` followed by the
        operator is stored. If operator is multiplicative, `1` followed by the
        operator is stored.
        If the last element in storage is already an operator, it is replaced.
        In all other cases operator is appended to storage.

        Arguments
        ---------
        operator : str
            Character should be of type operator
        """

        if len(self.__storage) == 0:
            self.__storage.extend([['1', '0']
                                  [self.__operators.index(character)//2],
                                   character])
        else:
            if self.__storage[-1] in self.__binary_operators:
                self.__storage[-1] = character
            else:
                self.__storage.append(character)

    def __apply_special(self, character) -> None:
        """Operations for characters of type special

        If special character is `AC` storage is cleared. `C` removes the last
        stored character. `i` performs multiplicative inverse on last character
        provided it is not an operator.

        Arguments
        ---------
        character : str
            Character should be either `AC`, `C` or `i`.
        """

        if len(self.__storage) == 0:
            return
        elif character == 'A':
            self.__storage.clear()
        elif character == 'C':
            self.__storage.pop(-1)
        elif character == 'i':
            self.__storage[-1] = str(neg(float(self.__storage[-1])))

    def __put_const(self, character):
        """Stores character of type constant

        If storage is empty or previous entry is operator constane is appended.
        Multiplier operator and then the constant is appended in other cases
        """

        character = self.__const[character]
        if len(self.__storage) == 0:
            self.__storage.append(character)
        elif self.is_not_digit(self.__storage[-1]):
            self.__storage.append(character)
        else:
            self.__storage.extend(['*', character])

    def __put_digit(self, character) -> None:
        """Stores character of type digit

        If previous entry to storage is not a digit the new character is
        appeded. Otherwise, new character is combined with the lat digit. For
        example if previous entry is `9` and latest entry is `8`, previous
        entry is modified to `98` and stored. If previous entry is `+` and new
        entry is `3`, `3` and `+` are stored seperately.

        Arguments
        ---------
        character : str
            Character must be of the type digit
        """

        if len(self.__storage) == 0:
            self.__storage.append(character)
        elif self.is_not_digit(self.__storage[-1]):
            self.__storage.append(character)
        else:
            self.__storage[-1] += character

    def __put_dot(self, dot='.'):
        """Logic for storing dot character.

        If dot is first entry, `0.` is stored. Otherwise dot is appended to
        previous entry, provided it is a digit. If dot already in previous
        entry latest dot is ignored.
        """

        if len(self.__storage) == 0:
            self.__storage.append("0.")
            return
        if ((self.__storage[-1] not in self.__operators) and
           (dot not in self.__storage[-1])):
            self.__storage[-1] += dot

    def __put_left_paren(self):
        """Appends right parenthesis in storage.

        Parenthesis is always stored independently. For example `(`, `3` is
        allowed while `(3` is not allowed."""

        LEFT_PAREN = "("
        if len(self.__storage) == 0:
            self.__storage.append(LEFT_PAREN)
            return
        elif self.__storage[-1] not in self.__operators:
            self.__storage.extend(['*', LEFT_PAREN])
            return
        self.__storage.append(LEFT_PAREN)

    def __put_right_paren(self):
        """Logic for adding left parenthesis in storage.

        Right parenthesis(R.P) is added to storage only if `count` of left
        parenthesis is more that the number of R.P in storage.
        """

        left_paren_count = self.__storage.count('(')
        right_paren_count = self.__storage.count(')')
        if left_paren_count > right_paren_count:
            self.__storage.append(')')
