import math
from typing import List


class ReversePolishNotation:
    def _is_integer(self, num: str):
        return num.isdigit() or (num.startswith('-') and num[1:].isdigit())

    def _operate(self, num1: int, num2: int, operation: str) -> int:
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            return int(num1 / num2)
        else:
            return -1

    def eval_rpn(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self._is_integer(token):
                stack.append(int(token))
            else:
                operator = token
                num2, num1 = int(stack.pop()), int(stack.pop())
                result = self._operate(num1, num2, operator)
                stack.append(result)
        return stack[-1]


nums_list = ["4", "13", "5", "/", "+"]
print(ReversePolishNotation().eval_rpn(nums_list))