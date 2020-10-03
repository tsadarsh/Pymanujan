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

    Methods
    -------
    calculate(expr_as_list: list, operators: list)
        Loops through expr_as_list until all operators are popped.
    """

    ans: str
    _get_value = {
            '^': lambda x, y: x**y,
            '/': lambda x, y: x/y,
            '*': lambda x, y: x*y,
            '+': lambda x, y: x+y,
            '-': lambda x, y: x-y
            }
    __operators: list = ['(' ,'^', '/', '*', '+', '-']

    def __init__(self, expr_as_list: list):
        """
        Attributes
        ----------
        expr_as_list: list
            a list of operators and operands as strings
        """

        self.expr_as_list = expr_as_list

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

        left_paren = self.__operators[0]
        while left_paren in self.expr_as_list:
            expression = self.__bracket_balencer(self.expr_as_list.copy())
            left_p = expression.index('(')
            right_p = (len(expression)
                       - list(reversed(expression)).index(')') - 1)
            sub_expression = expression[left_p+1:right_p]
            new_instance = Calculate(sub_expression)
            self.expr_as_list[left_p:right_p+1] = [
                    new_instance.calculate()
                    ]

        exponent = self.__operators[1]
        while exponent in self.expr_as_list:
            index = self.expr_as_list.index(exponent)
            self.__partial_calculate(index)

        div_mul_op = self.__operators[2:4]
        gen_mul_div = (g for g in div_mul_op if g in self.expr_as_list)
        while any(gen_mul_div):
            index = self.expr_as_list.index(self.__operators[1])
            self.__partial_calculate(index)

        add_sub_op = self.__operators[4:6]
        gen_add_sub = (g for g in add_sub_op if g in self.expr_as_list)
        while any(gen_add_sub):
            index = self.expr_as_list.index(self.__operators[3])
            self.__partial_calculate(index)

        self.ans = self.expr_as_list[0]
        return self.ans

    def __partial_calculate(self, index: int) -> None:
        print(self.expr_as_list)
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

    def __bracket_balencer(self, expression: list):
        left_paren_count = expression.count('(')
        right_paren_count = expression.count(')')
        right_paren = ')'
        if left_paren_count > right_paren_count:
            count_diff = left_paren_count - right_paren_count
            expression.extend(right_paren * count_diff)
            return expression
        return expression
