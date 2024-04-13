class Node:
    """
    Node class
    """
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Queue:
    """
    Queue class
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        """
        Check whether the queue is empty
        """
        return self.head is None

    def add(self, item):
        """
        Add item to queue
        """
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def pop(self):
        """
        Remove first item from the queue
        """
        if self.head:
            item = self.head.item
            self.head = self.head.next
            return item
        raise ValueError('Queue is empty.')

    @property
    def peek(self):
        """
        Return the first item of the queue
        """
        return self.head.item

    def __len__(self):
        """
        Quantity of itmes in the queue
        """
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        s = ''
        current = self.head
        while current is not None:
            s += str(current.item)+' '
            current = current.next
        return f'start -> {s}<- end'

class MyStack:
    """
    Stack from queue implementation
    """
    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        """
        Method to add item to the end of the stack
        """
        self.queue.add(x)

    def pop(self) -> int:
        """
        Method to delete last el from stack
        """
        if len(self.queue) == 0:
            return None
        elif len(self.queue) == 1:
            return self.queue.pop()
        else:
            size = len(self.queue)
            for _ in range(size - 1):
                self.queue.add(self.queue.pop())
            return self.queue.pop()

    def top(self) -> int:
        """
        Method to return the top element of the stack without removing it
        """
        if len(self.queue) == 0:
            return None
        if len(self.queue) == 1:
            return self.queue.peek
        size = len(self.queue)
        for _ in range(size - 1):
            self.queue.add(self.queue.pop())
        top = self.queue.peek
        self.queue.add(self.queue.pop())
        return top

    def empty(self) -> bool:
        """
        Method to check whether the stack is empty
        """
        return len(self.queue) == 0
