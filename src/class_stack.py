class Stack(list):

    def push(self, x: int) -> None:
        return self.append(x)

    def pop(self) -> int:
        if len(self) == 0:
            raise IndexError("Error: stack is empty")
        return super().pop()

    def peek(self) -> int:
        if len(self) == 0:
            raise IndexError("Error: stack is empty")
        return self[-1]

    def is_empty(self) -> bool:
        if len(self) == 0:
            return True
        else:
            return False

    def __len__(self) -> int:
        return super().__len__()


    def min(self) -> int:
        if len(self) == 0:
            raise IndexError("Error: stack is empty")
        return min(self)

