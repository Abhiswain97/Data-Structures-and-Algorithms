import operator
from typing import Dict, List


class InfixToPostfix:
    def __init__(self, expr: str):
        self.expr: List[str] = expr.split()
        self.stack: List[str] = []
        self.precedence: Dict[str, int] = {"+": 1, "-": 1, "*": 2, "/": 2}
        self.postfix: str = str()

    def _size(self) -> int:
        return len(self.stack)

    def _stack_push(self, data: str) -> None:
        self.stack.append(data)

    def _stack_pop(self) -> None:
        self.stack.pop()

    def _stack_top(self) -> str:
        return self.stack[-1]

    def _check_if_operator(self, ch: str) -> bool:
        return ch in self.precedence.keys()

    def _has_higher_precedence(self, top: str, ch: str) -> bool:
        return self.precedence[top] > self.precedence[ch]

    def convert(self) -> str:
        for c in self.expr:
            if not self._check_if_operator(c):
                self.postfix += c
            else:
                while self._size() != 0 and self._has_higher_precedence(
                    self._stack_top(), c
                ):
                    self.postfix += self._stack_top()
                    self._stack_pop()

                self._stack_push(c)

        while self._size() != 0:
            self.postfix += self._stack_top()
            self._stack_pop()

        return self.postfix


if __name__ == "__main__":
    s = "A + B * C - D + E"

    res = InfixToPostfix(s).convert()

    print(f"Postfix expression: {res}")
