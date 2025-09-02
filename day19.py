def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.lstrip("-").isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))

    return stack[0]


if __name__ == "__main__":
    expression = input().strip()
    print(evaluate_postfix(expression))
