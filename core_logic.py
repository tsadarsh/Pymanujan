import logging

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
        try:
            right_operand = float(self.expr_as_list[index+1])
            sub_result = self._get_value[operator](left_operand, right_operand)
            self.expr_as_list[index-1:index+2] = [str(sub_result)]
        except IndexError:
            self.expr_as_list[index-1:index+2] = [str(left_operand)]
