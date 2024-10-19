class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "La pila está vacía."

    def is_empty(self):
        return len(self.stack) == 0

mi_pila = Stack()

mi_pila.push(10)
mi_pila.push(20)
mi_pila.push(30)

print(f"El tope de la pila es: {mi_pila.peek()}")