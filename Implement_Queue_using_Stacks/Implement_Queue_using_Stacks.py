class Node:
    """
    Node class
    """
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Stack:
    """
    Stack class
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Check if the stack is empty
        """
        return self.head is None

    def push(self, item):
        """
        Add el to the end of the stack
        """
        self.head = Node(item, self.head)

    def pop(self):
        """
        Deletes last el from the stack
        """
        item = self.head.item
        self.head = self.head.next
        return item

    @property
    def peek(self):
        """
        Returns the last el without del
        """
        return self.head.item

    def __len__(self):
        """
        Get the quantity of el in stack
        """
        count = 0
        current = self.head
        while current is not None:
            count +=1
            current = current.next
        return count

    def __str__(self):
        s = ''
        cur = self.head
        while cur is not None:
            s = str(cur.item) + ' ' +s
            cur = cur.next
        return 'bottom -> '+ s+'<- top'

class MyQueue:
    """
    Queue from Stack class
    """
    def __init__(self):
        self.back_stack = Stack()
        self.front_stack = Stack()

    def push(self, x):
        """
        Add el to the end of the queue
        """
        while not self.front_stack.is_empty():
            self.back_stack.push(self.front_stack.pop())
        self.back_stack.push(x)

    def pop(self):
        """
        Deletes 1st el from the queue
        """
        while not self.back_stack.is_empty():
            self.front_stack.push(self.back_stack.pop())
        return self.front_stack.pop()

    def peek(self):
        """
        Returns the first el without del
        """
        while not self.back_stack.is_empty():
            self.front_stack.push(self.back_stack.pop())
        return self.front_stack.peek

    def empty(self):
        """
        Check if the queue is empty
        """
        return self.back_stack.is_empty() and self.front_stack.is_empty()