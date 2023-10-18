class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

def evaluate_postfix(expression):
    stack = Stack()
    operators = {'+', '-', '*', '/'}

    for token in expression.split():
        if token.isdigit() or (token[1:].isdigit() and token[0] == '-'):
            stack.push(int(token))  # Push operand onto the stack
        elif token in operators:
            if stack.is_empty():
                raise ValueError("Invalid expression: not enough operands")
            operand2 = stack.pop()
            if stack.is_empty():
                raise ValueError("Invalid expression: not enough operands")
            operand1 = stack.pop()
            result = evaluate_operation(token, operand1, operand2)
            stack.push(result)
        else:
            raise ValueError(f"Invalid token: {token}")

    if stack.is_empty() or len(stack.items) > 1:
        raise ValueError("Invalid expression: too many operands")

    return stack.peek()

def evaluate_operation(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            raise ValueError("Division by zero is not allowed")
        return operand1 / operand2

# Example usage:
postfix_expression = "6 5 2 3 + 8 * - *"
result = evaluate_postfix(postfix_expression)
print(f"Result: {result}")  # Output: Result: 28
