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
            'x!': lambda x, y: Calculate.factorial(None,int(x),int(y)),
            '^': lambda x, y: x**y,
            '/': lambda x, y: x/y,
            '*': lambda x, y: x*y,
            '+': lambda x, y: x+y,
            '-': lambda x, y: x-y
            }
    __operators: list = ['(', '^', '/', '*', '+', '-', 'x!']

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

        fact_op = self.__operators[6]
        if any(fact_op):
            self.__call_partial_calculate(fact_op)
        exp_op = self.__operators[1]
        gen_exp = self.__create_op_gen(exp_op)
        if any(gen_exp):
            self.__call_partial_calculate(exp_op)

        div_mul_op = self.__operators[2:4]
        gen_mul_div = self.__create_op_gen(div_mul_op)
        if any(gen_mul_div):
            self.__call_partial_calculate(div_mul_op)

        add_sub_op = self.__operators[4:6]
        gen_add_sub = self.__create_op_gen(add_sub_op)
        if any(gen_add_sub):
            self.__call_partial_calculate(add_sub_op)

        self.ans = self.expr_as_list
        return self.ans[0]

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

    def __bracket_balencer(self, expression: list):
        left_paren_count = expression.count('(')
        right_paren_count = expression.count(')')
        right_paren = ')'
        if left_paren_count > right_paren_count:
            count_diff = left_paren_count - right_paren_count
            expression.extend(right_paren * count_diff)
            return expression
        return expression

    def __call_partial_calculate(self, operator):
        while True:
            indices = (i for i, e in enumerate(self.expr_as_list) if
                       e in operator)
            index = next(indices, False)
            if not index:
                break
            self.__partial_calculate(index)

    def __create_op_gen(self, operator: list):
        generator = (g for g in operator if g in self.expr_as_list)
        return generator

    def factorial(self, num, num2):
        print(self, num, num2)
        result = 1
        for i in range(1, num + 1):
            result = result * i
        print(result)
        return result

