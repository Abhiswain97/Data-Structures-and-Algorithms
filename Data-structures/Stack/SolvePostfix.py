"""
Does not support decimal division, works only for operators +, -, /(floor divison), *
"""

import operator
from typing import Dict, List, Tuple, Type


class SolvePostfix:
    def __init__(self):
        self.data: List[int] = []
        self.operators: Dict[str] = {
            "+": operator.add,
            "-": operator.sub,
            "/": operator.floordiv,
            "*": operator.mul,
        }

    def check(self, ch: str) -> bool:
        return ch in self.operators.keys()

    def push(self, data: int) -> None:
        self.data.append(data)

    def pop_stack(self) -> Tuple[int, int]:
        val1 = self.data.pop()
        val2 = self.data.pop()

        return val1, val2

    def fail_check(self, expr: List[str]) -> bool:
        return expr[-2] not in self.operators.keys()

    def solve(self, expr: str):
        """
        `expr`: should be a space separated character string

        eg:
           "1 2 * 2 3 + 12 2 * -"  
        """
        expr_list: List[str] = expr.split()

        if self.fail_check(expr_list):
            print(
                "[Warning]: No operator specified for the last two operands. So the result will the output of the last operation."
            )

        for c in expr_list:
            if self.check(c):
                v1, v2 = self.pop_stack()

                print(f"Solving {v1} {c} {v2}")

                res = self.operators[c](v1, v2)
                self.push(res)
            else:
                self.push(int(c))

        return self.data.pop()


if __name__ == "__main__":
    s = "1 2 * 2 3 + 12 2 * -"

    solver = SolvePostfix()
    res = solver.solve(s)

    print(f"Result = {res}")
