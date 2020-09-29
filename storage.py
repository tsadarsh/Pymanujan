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

    __operators: list = ['/', '*', '+', '-']
    __special: list = ['C', 'A', 'i']
    __storage: list
    __result: str

    def __init__(self):
        self.__storage = []

    def show_storage(self) -> str:
        """Returns stored characters as a single formatted string.

        Elements from a list containing stored characters are combined to a
        single string with whitespace around operators.
        """

        this = ''.join(
                       map(
                           lambda i: ' '+i+' ' if i in self.__operators else i,
                           self.__storage)
                           )
        return this

    def show_storage_as_list(self) -> list:
        """Returns stored characters as a list"""

        return self.__storage

    def into_storage(self, character: str) -> None:
        """Stores argument `character` if logic is met.

        Logic checks if `character` is operator, special or dot and applies
        necessary operations internally. Private-method(p.m) `put_operator`
        is called if logic identifies `character` as an operator. Similarly,
        p.m `apply_special`, `put_dot` and `put_digit` is called when logic
        identifies a special, dot and digit char respectively.

        Arguments
        ---------
        character : str
            Character to be stored
        """

        if character in self.__operators:
            return self.__put_operator(character)
        if character in self.__special:
            return self.__apply_special(character)
        if character is '.':
            return self.__put_dot(character)
        if character == '(':
            return self.__put_left_paren()
        if character == ')':
            return self.__put_right_paren()
        if not character.isnumeric() and character != '.':
            raise ValueError
        return self.__put_digit(character)

    def is_not_digit(self, item: str):
        try:
            float(item)
            return False
        except ValueError:
            return True

    def __put_operator(self, character) -> None:
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
            if self.__storage[-1] in self.__operators:
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

    def __put_digit(self, character) -> None:
        """Stores chracter of type digit

        If previous entry to storage is a charater of type digit the new
        character is appeded. Otherwise, new character is added as a new entry.
        For example if previous entry is `9` and latest entry is `8`, previous
        entry is modified to `98` and stored.

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
        self.__storage.append("(")

    def __put_right_paren(self):
        left_paren_count = self.__storage.count('(')
        right_paren_count = self.__storage.count(')')
        if left_paren_count > right_paren_count:
            self.__storage.append(')')
