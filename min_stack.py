from typing import Tuple


class MinStack:
    def __init__(self):
        self.stack = []

    def _top(self) -> Tuple:
        return self.stack[-1]

    def push(self, val: int) -> None:
        min_val = min(val, self.get_min()) if self.stack else val
        self.stack.append((val, min_val))
        print("Added " + str(val) + " to the stack. \n"
                                    "Current Min Value in stack is " + str(self.get_min()))
        print()

    def pop(self) -> None:
        print("Removing " + str(self.top()) + " from the stack")
        self.stack.pop()
        print("Removed")
        print()

    def top(self) -> int:
        return self._top()[0]

    def get_min(self) -> int:
        return self._top()[1]


stack = MinStack()
print("Pushing to stack >>> ")
stack.push(3)
stack.push(6)
stack.push(1)
stack.push(2)
stack.push(4)
for _ in range(3):
    stack.pop()
    print("Min in stack: " + str(stack.get_min()))
    print()
print("Top element: " + str(stack.top()))
