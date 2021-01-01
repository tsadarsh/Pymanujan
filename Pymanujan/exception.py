class ExpressionNotCalculatedCompletely(Exception):
    def __init__(self, expression):
        self.message = expression
        super().__init__(self.message)
