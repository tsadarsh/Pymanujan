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
        elif character == self.__left_paren:
            return self.__put_left_paren()
        elif character == self.__right_paren:
            return self.__put_right_paren()
        elif character.isnumeric():
            return self.__put_digit(character)
        else:
            raise ValueError

    def is_not_digit(self, item: str):
        """Returns True if string passed is not integer or float.

        Arguments
        ---------
        item : str
            String datatype to check if not integer or not float
        """
        try:
            float(item)
            return False
        except ValueError:
            return True

    def __put_unary_operator(self, un_opr: str) -> None:
        if len(self.__storage) == 0:
            self.__storage.append(un_opr)
        elif not self.is_not_digit(self.__storage[-1]):
            if un_opr == '!':
                self.__storage.append(un_opr)
            else:
                self.__storage.extend(['*', un_opr])
        elif self.__storage[-1] in self.__unary_operators:
            if un_opr == '!':
                self.__storage.extend(['*', '(', '1', un_opr])
            self.__storage.extend(['*', '(', un_opr])
        else:
            self.__storage.append(un_opr)

    def __put_binary_operator(self, bin_opr: str) -> None:
        """Logic for characters of type binary for storing

        In case storage is empty, if operator is addive, `0` followed by the
        operator is stored. If operator is multiplicative, `1` followed by the
        operator is stored.
        If the previous element in storage is an operator, it is replaced.
        In all other cases operator is appended to storage.

        Arguments
        ---------
        operator : str
            Character of type binary_operator
        """

        if len(self.__storage) == 0:
            self.__storage.extend([['1', '0']
                                  [self.__operators.index(bin_opr)//2],
                                   bin_opr])
        else:
            if self.__storage[-1] in self.__binary_operators:
                self.__storage[-1] = bin_opr
            else:
                self.__storage.append(bin_opr)

    def __apply_special(self, special: str) -> None:
        """Operations for characters of type special

        If special character is `A` storage is cleared. `C` removes the last
        stored character. `i` performs multiplicative inverse on last character

        Arguments
        ---------
        special : str
            Character should be either `A`, `C` or `i`.
        """

        if len(self.__storage) == 0:
            return
        elif special == 'A':
            self.__storage.clear()
        elif special == 'C':
            self.__storage.pop(-1)
        elif special == 'i':
            self.__storage[-1] = str(neg(float(self.__storage[-1])))

    def __put_const(self, const_repr: str) -> None:
        """Stores character of type constant

        If storage is empty or previous entry is operator constant is appended.
        Multiplier operator and then the constant is appended in other cases

        Arguments
        ---------
        character : str
            Character of type `const`
        """

        const = self.__const[const_repr]
        if len(self.__storage) == 0:
            self.__storage.append(const)
        elif self.is_not_digit(self.__storage[-1]):
            self.__storage.append(const)
        else:
            self.__storage.extend(['*', const])

    def __put_digit(self, digit: str) -> None:
        """Stores character of type digit

        If previous entry to storage is not a digit the new character is
        appeded. Otherwise, new character is combined with the last digit. For
        example if previous entry is `9` and latest entry is `8`, previous
        entry is modified to `98` and stored. If previous entry is `+` and new
        entry is `3`, `3` and `+` are stored as seperate elements.

        Arguments
        ---------
        digit : str
            Character of the type `digit`
        """

        if len(self.__storage) == 0:
            self.__storage.append(digit)
        elif self.is_not_digit(self.__storage[-1]):
            self.__storage.append(digit)
        else:
            self.__storage[-1] += digit

    def __put_dot(self, dot: str) -> None:
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
        """Appends left parenthesis in storage.

        If previous element is of type digit, multiplication operator followed
        by left parenthesis is appended in storage.
        """

        if len(self.__storage) == 0:
            self.__storage.append(self.__left_paren)
            return
        elif self.__storage[-1] not in self.__operators:
            self.__storage.extend(['*', self.__left_paren])
            return
        self.__storage.append(self.__left_paren)

    def __put_right_paren(self):
        """Logic for adding right parenthesis in storage.

        Right parenthesis is added to storage only if count of left
        parenthesis is more than count of right parenthesis.
        """

        left_paren_count = self.__storage.count(self.__left_paren)
        right_paren_count = self.__storage.count(self.__right_paren)
        if left_paren_count > right_paren_count:
            self.__storage.append(self.__right_paren)
