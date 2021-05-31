import operator


class SolvePostfix:
    def __init__(self):
        self.data = []
        self.operators = {'+': operator.add, '-': operator.sub,
                          '/': operator.floordiv, '*': operator.mul}

    def check(self, ch):
        return ch in self.operators.keys()

    def push(self, data):
        self.data.append(data)

    def pop_stack(self):
        val1 = self.data.pop()
        val2 = self.data.pop()

        return val1, val2

    def fail_check(self, expr):
        return expr[-2] not in self.operators.keys()

    def solve(self, expr: str):
        """
        `expr`: should be a space separated character string

        eg:
           "1 2 * 2 3 + 12 2 * -"  
        """
        expr = expr.split()

        if self.fail_check(expr):
            print("[Warning]: No operator specified for the last two operands. So the result will the output of the last operation.")

        for c in expr:
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
