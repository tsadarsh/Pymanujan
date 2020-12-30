import math


from exception import ExpressionNotCalculatedCompletely


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

    _get_value = {
            'sin': lambda x: math.sin(math.radians(x)),
            'cos': lambda x: math.cos(math.radians(x)),
            'tan': lambda x: math.tan(math.radians(x)),
            'asin': lambda x: math.degrees(math.asin(x)),
            'acos': lambda x: math.degrees(math.acos(x)),
            'atan': lambda x: math.degrees(math.atan(x)),
            '!': lambda x: math.factorial(x),
            'log': lambda x: math.log10(x),
            'ln': lambda x: math.log(x),
            '^': lambda x, y: x**y,
            '/': lambda x, y: x/y,
            '*': lambda x, y: x*y,
            '+': lambda x, y: x+y,
            '-': lambda x, y: x-y
            }
    __unary_operators = ['sin', 'cos', 'tan', 'asin', 'acos',
                         'atan', '!', 'log', 'ln']
    __operators: list = ['(', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan',
                         '!', 'log', 'ln', '^', '/', '*', '+', '-']

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
        a new instance of Calculate. BODMAS rule is followed to pop operators.
        If operator identified `partial_calculate` if
        found. After passing all the while loops it is assumed expr_as_list has
        no more operators. Only one element(answer) remains in expr_as_list,
        expr_as_list[0] is returned.
        """

        # parenthesis operator identification
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

        # unary operator identification
        unary_op = self.__operators[1:10]
        gen_unary = self.__create_op_gen(unary_op)
        if any(gen_unary):
            self.__call_partial_calculate(unary_op)

        # exponent operator identification
        exp_op = self.__operators[10]
        gen_exp = self.__create_op_gen(exp_op)
        if any(gen_exp):
            self.__call_partial_calculate(exp_op)

        # division and multiplication operator identification
        div_mul_op = self.__operators[11:13]
        gen_mul_div = self.__create_op_gen(div_mul_op)
        if any(gen_mul_div):
            self.__call_partial_calculate(div_mul_op)

        # addition and subtraction operator identification
        add_sub_op = self.__operators[13:15]
        gen_add_sub = self.__create_op_gen(add_sub_op)
        if any(gen_add_sub):
            self.__call_partial_calculate(add_sub_op)

        if len(self.expr_as_list) == 1:
            final_answer = self.expr_as_list[0]
            return final_answer
        else:
            current_expression = self.expr_as_list
            raise ExpressionNotCalculatedCompletely(current_expression)

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
        # unary opreator calculation
        if operator in self.__unary_operators:
            if operator != '!':
                unary_operand = float(self.expr_as_list[index+1])
                sub_result = self._get_value[operator](unary_operand)
                self.expr_as_list[index: index+2] = [str(sub_result)]
            else:
                unary_operand = int(self.expr_as_list[index-1])
                sub_result = self._get_value[operator](unary_operand)
                self.expr_as_list[index-1: index+1] = [str(sub_result)]
            return

        # all other operator with two operands
        left_operand = float(self.expr_as_list[index-1])
        try:
            right_operand = float(self.expr_as_list[index+1])
            sub_result = self._get_value[operator](left_operand, right_operand)
            self.expr_as_list[index-1:index+2] = [str(sub_result)]
        except IndexError:
            self.expr_as_list[index-1:index+2] = [str(left_operand)]

    def __bracket_balencer(self, expression: list):
        """Appends closing parenthesis to equal number of opening parenthesis.

        This logic only handles cases where number of operning parenthesis is
        more that number of closing parenthesis. The GUI should ensure closing
        parenthesis is not entered in the absence of opening counterpart.
        """
        left_paren_count = expression.count('(')
        right_paren_count = expression.count(')')
        right_paren = ')'
        if left_paren_count > right_paren_count:
            count_diff = left_paren_count - right_paren_count
            expression.extend(right_paren * count_diff)
            return expression
        return expression

    def __call_partial_calculate(self, found_operator: str):
        """Logic to parse every `found_operator` in expression list.

        After operator is found, the expression is parsed recursively while
        all the operators of same kind are `partial_calculate`d and substituted
        with the partial answer.

        Example
        -------
        found_operator = '+'
        expr_as_list = ['4', '+', '3', '-', '10', '+', '2']
        Here expr_as_list is modified to ['7', '-', '12'] after ['4', '+', '3']
        and ['10', '+', '2'] partial expression are calculated and substituted
        in places where `found_operator` exists.

        Arguments
        ---------
        found_operator : str
            Operator to substitute in expression
        """
        FOUND_OPERATOR_EXISTS = True
        while FOUND_OPERATOR_EXISTS:
            for index, operator in enumerate(self.expr_as_list):
                if operator in found_operator:
                    self.__partial_calculate(index)
                    break
            else:
                FOUND_OPERATOR_EXISTS = False

    def __create_op_gen(self, operator: list):
        generator = (g for g in operator if g in self.expr_as_list)
        return generator
