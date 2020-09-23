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
    __special: list = ['C', 'AC', 'i']
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
        if not character.isnumeric() and character != '.':
            raise ValueError
        return self.__put_digit(character)

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
            ''' First entry to __storage '''
            self.__storage.extend([['1', '0']
                                  [self.__operators.index(character)//2],
                                   character])
        else:
            ''' Not first input '''
            if self.__storage[-1] in self.__operators:
                ''' Changing 3+- to 3- '''
                self.__storage[-1] = character
            else:
                ''' DEFAULT: Adding operator '''
                self.__storage.append(character)

    def __apply_special(self, special) -> None:
        if special == 'AC':
            self.__storage.clear()
        if special == 'C':
            self.__storage.pop(-1)
        if special == 'i':
            ''' Multiplicative inverse of last number chunk.
            Diabled when last input is operator '''
            self.__storage[-1] = str(neg(float(self.__storage[-1])))

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
