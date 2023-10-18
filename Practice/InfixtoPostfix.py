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

def is_operator(char):
    return char in {'+', '-', '*', '/'}

def precedence(operator):
    return {'+': 1, '-': 1, '*': 2, '/': 2}.get(operator, 0)

def infix_to_postfix(infix_expression):
    output = []
    stack = Stack()

    for char in infix_expression:
        if char.isalpha():
            output.append(char)
        elif is_operator(char):
            while not stack.is_empty() and is_operator(stack.peek()) and precedence(stack.peek()) >= precedence(char):
                output.append(stack.pop())
            stack.push(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            if not stack.is_empty() and stack.peek() == '(':
                stack.pop()  # Discard the opening parenthesis
        else:
            raise ValueError(f"Invalid character: {char}")

    while not stack.is_empty():
        if stack.peek() == '(':
            raise ValueError("Mismatched parentheses in the expression")
        output.append(stack.pop())

    return "".join(output)

# Example usage:
infix_expression = "a*b+c"
postfix_expression = infix_to_postfix(infix_expression)
print(f"Infix Expression: {infix_expression}")
print(f"Postfix Expression: {postfix_expression}")