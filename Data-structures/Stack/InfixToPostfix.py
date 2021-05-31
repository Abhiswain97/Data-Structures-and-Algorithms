import operator


class InfixToPostfix:
    def __init__(self):
        self.stack = []
        self.precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
        self.operators = ["+", "-", "/", "*"]
        self.postfix = str()

    def _size(self):
        return len(self.stack)

    def _stack_push(self, stack):
        self.stack.append(stack)

    def _stack_pop(self):
        self.stack.pop()

    def _stack_top(self):
        return self.stack[-1]

    def _check_if_operator(self, ch):
        return ch in self.operators

    def has_higher_precedence(self, top, ch):
        return self.precedence[top] > self.precedence[ch]

    def convert(self, expr: str):
        expr = expr.split()

        for c in expr:
            if not self._check_if_operator(c):
                self.postfix += c
            else:
                while self._size() != 0 and self.has_higher_precedence(
                    self._stack_top(), c
                ):
                    self.postfix += self._stack_top()
                    self._stack_pop()

                self._stack_push(c)

        while self._size() != 0:
            self.postfix += self._stack_top()
            self._stack_pop()


if __name__ == "__main__":
    s = "A + B * C - D + E"

    solver = InfixToPostfix()

    solver.convert(s)

    print(f"Postfix expression: {solver.postfix}")
