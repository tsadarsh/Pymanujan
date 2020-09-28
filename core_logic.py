class Calculate():
    """Class to compute final asnwer from list of operands and operators

    This class calulates final answer from list of operands and operators by
    slicing expr_as_list to partial expression containing a left-operand, an
    operator and a right-operand one at a time. This process continues untill
    expr_as_list contains no element present in 'operators'.

    Attributes
    ----------
    expr_as_list: list
        a list of operators and operands as strings
    operators: list
        a list of valid operators as strings

    Methods
    -------
    calculate(expr_as_list: list, operators: list)
        Loops through expr_as_list until all operators are popped.
    """

    ans: str
    _get_value = {
            '/': lambda x, y: x/y,
            '*': lambda x, y: x*y,
            '+': lambda x, y: x+y,
            '-': lambda x, y: x-y
            }

    def __init__(self, expr_as_list: list, operators: list):
        """
        Attributes
        ----------
        expr_as_list: list
            a list of operators and operands as strings
        operators: list
            a list of valid operators as strings
        """

        self.expr_as_list = expr_as_list
        self.operators = operators

    def calculate(self) -> str:
        """Loops through expr_as_list until all operators are popped.

        Elements between parenthesis is sent as a seperate `sub_expression` to
        a new instance of Calculate.
        Operators are popped in the following order: '/', '*', '+', '-'. While
        loop checks the presence of operators and calls __partial_calculate if
        found. After passing all the while loops it is assumed expr_as_list has
        no more operators. Only one element(answer) remains in expr_as_list,
        expr_as_list[0] is returned.
        """

        if '(' in self.expr_as_list:
            expression = self.expr_as_list.copy()
            left_p = expression.index('(')
            if ')' not in self.expr_as_list:
                self.expr_as_list.pop(left_p)
            else:
                right_p = (len(expression)
                           - list(reversed(expression)).index(')') - 1)
                sub_expression = expression[left_p+1:right_p]
                new_instance = Calculate(sub_expression, self.operators)
                self.expr_as_list[left_p:right_p+1] = [
                        new_instance.calculate()
                        ]

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

    def __partial_calculate(self, index: int) -> None:
        """Computes single chunk of expression from provided operator index

        From given operator index, left and right operand index assumes index-1
        and index+1 values. Chunk now constitutes left-operand, operator and
        right-operand. _get_value dictionary returns calulated chunk value from
        operator passed as key.

        Parameters
        ----------
        index: int
            Index value of operator

        Raises
        ------
        IndexError
            If there is no operand next to operator
        """

        operator = self.expr_as_list[index]
        left_operand = float(self.expr_as_list[index-1])
        try:
            right_operand = float(self.expr_as_list[index+1])
            sub_result = self._get_value[operator](left_operand, right_operand)
            self.expr_as_list[index-1:index+2] = [str(sub_result)]
        except IndexError:
            self.expr_as_list[index-1:index+2] = [str(left_operand)]
