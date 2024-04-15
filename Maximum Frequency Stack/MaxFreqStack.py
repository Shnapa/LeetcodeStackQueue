from collections import deque

class FreqStack:
    """
    Freqstack class
    """
    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        """
        Push method
        """
        self.stack.append(val)

    def pop(self) -> int:
        """
        Pop method
        """
        if not self.stack:
            return None

        cop = self.stack.copy()
        cop.reverse()
        max_count = max(cop, key=lambda x: self.stack.count(x))
        other_q = deque()
        while (v := self.stack.pop()) != max_count:
            other_q.append(v)
        while other_q:
            self.stack.append(other_q.pop())
        return max_count