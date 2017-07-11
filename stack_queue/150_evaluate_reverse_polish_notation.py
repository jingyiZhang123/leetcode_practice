"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens:
            if token in '+-*/':
                arg2 = stack.pop()
                arg1 = stack.pop()
                if token == '+':
                    stack.append(arg1 + arg2)
                elif token == '-':
                    stack.append(arg1 - arg2)
                elif token == '*':
                    stack.append(arg1 * arg2)
                else:
                    stack.append(int(float(arg1) / arg2))
            else:
                stack.append(int(token))
        return stack.pop()




print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))




