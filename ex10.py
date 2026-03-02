class Queue:
    def __init__(self, max_size=100):
        self.__data = [None] * max_size
        self.__max_size = max_size
        self.__front = 0
        self.__rear = -1
        self.__size = 0

    @property
    def max_size(self):
        return self.__max_size

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Fila excedeu o tamanho máximo")
        self.__rear = (self.__rear + 1) % self.__max_size
        self.__data[self.__rear] = item
        self.__size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Fila vazia")
        item = self.__data[self.__front]
        self.__data[self.__front] = None
        self.__front = (self.__front + 1) % self.__max_size
        self.__size -= 1
        return item

    def peek(self):
        if not self.is_empty():
            return self.__data[self.__front]
        else:
            raise IndexError("Fila vazia")
    def is_empty(self):
        return self.__size == 0
    def is_full(self):
        return self.__size >= self.__max_size
    def __str__(self):
        return (
            f"Dados: {self.__data}, "
            f"Tamanho: {self.__size}, "
            f"Frente: {self.__front}, "
            f"Traseira: {self.__rear}."
        )

queue = Queue(max_size=5)
try:
    queue.enqueue(1)
    print(queue)
    queue.enqueue(2)
    print(queue)
    queue.enqueue(3)
    print(queue)
    queue.enqueue(4)
    print(queue)
    queue.enqueue(5)
    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    print(queue)
    queue.enqueue(1)
    print(queue)
    queue.enqueue(2)
    print(queue)
    queue.enqueue(3)
    print(queue)
    queue.enqueue(4)
    print(queue)
    queue.enqueue(5)
    print(queue)
except (OverflowError, IndexError) as e:
    print(e)
