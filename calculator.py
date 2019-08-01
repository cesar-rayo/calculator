class CalculatorError(Exception):
    """Exception class"""

import numbers
import sys

class Calculator:
    def add(self, a, b):
        try:
            self._check_operand(a)
            self._check_operand(b)
            return a + b
        except TypeError as ex:
            raise CalculatorError("Invalid types")

    def subtract(self, a, b):
        try:
            self._check_operand(a)
            self._check_operand(b)
            return a - b
        except TypeError as ex:
            raise CalculatorError("Invalid types")

    def multiply(self, a, b):
        try:
            self._check_operand(a)
            v_check_operand(b)
            return a * b
        except TypeError as ex:
            raise CalculatorError("Invalid types")

    def divide(self, a, b):
        try:
            self._check_operand(a)
            self._check_operand(b)
            return a / b
        except TypeError as ex:
            raise CalculatorError("Invalid types")
        except ZeroDivisionError as ex:
            raise CalculatorError("Can not divide by zero!")

    def _check_operand(self, operator):
        if not isinstance(operator, numbers.Number):
            raise CalculatorError("'{}' is not a number".format(operator))

if __name__ == '__main__':

    calc = Calculator()
    operations = [
        calc.add,
        calc.subtract,
        calc.multiply,
        calc.divide
    ]
    while True:
        for i, operation in enumerate(operations, start = 1):
            print("{}. {}".format(i, operation.__name__))
        print("q. quit")

        option = input("Pick an operation: ")

        if option == 'q':
            sys.exit()
        else:
            try:
                op = int(option)
                a = int(input("'a' is: "))
                b = int(input("'b' is: "))
                result = operations[op - 1](a, b)
                print("==>> Result: '{}'".format(result))
            except IndexError as ex:
                print("Invalid Option")
            except CalculatorError as ex:
                print(ex)

