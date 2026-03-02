class Stack:
    def __init__(self, max_size=100):
        self.__data = []
        self.__max_size = max_size

    @property
    def max_size(self):
        return self.__max_size

    def push(self, item):
        if self.is_full():
            raise OverflowError("Pilha excedeu o tamanho máximo")
        self.__data.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__data.pop()
        else:
            raise IndexError("Pilha vazia")

    def peek(self):
        if not self.is_empty():
            return self.__data[-1]
        else:
            raise IndexError("Pilha vazia")

    def size(self):
        return len(self.__data)

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() >= self.__max_size

    def __str__(self):
        return (
            f"Dados: {self.__data}"
            f"Tamanho: {self.size()},"
            f"Topo: {self.peek() if not self.is_empty() else 'Pilha vazia'}."
        )

def reverse_text(text):
    stack = Stack(len(text))
    reversed = ""
    for char in text:
        stack.push(char)
    for char in range(stack.max_size):
        reversed += stack.pop()
    return reversed

print(reverse_text("ola"))
print(reverse_text("Hello World"))
print(reverse_text("live"))