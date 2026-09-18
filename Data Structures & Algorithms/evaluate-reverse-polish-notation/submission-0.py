class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = []
        operators = {"+", "-", "*", "/"}
        for n in tokens:
            if n in operators:
                right = total.pop()
                left = total.pop()
                if n == "+":
                    total.append(left + right)
                elif n == "*":
                    total.append(left * right)
                elif n == "-":
                    total.append(left - right)
                else:
                    total.append(int(left/right))
            else:
                total.append(int(n))
        return total[0]        