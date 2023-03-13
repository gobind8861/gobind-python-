class Stack:
    def __init__(self):
        self.gobindItems = []

    def push(self, item):
        self.gobindItems[len(self.gobindItems):]= [item]

    def pop(self):
        if not self.is_empty():
            item = self.gobindItems[-1]
            self.gobindItems = self.gobindItems[:len(self.gobindItems)-1]
            return item

    def peek(self):
        if not self.is_empty():
            return self.gobindItems[0]

    def is_empty(self):
        return len(self.gobindItems) == 0


def main():
    # create a new stack
    stack = Stack()

    # push some items onto the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # peek at the top item
    print(stack.peek())  # output: 3

    # pop an item off the stack
    print(stack.pop())   # output: 3

    # peek at the top item again
    print(stack.peek())  # output: 2

    # pop another item off the stack
    print(stack.pop())   # output: 2

    # check if the stack is empty
    print(stack.is_empty())  # output: False

    # pop the last item off the stack
    print(stack.pop())   # output: 1

    # check if the stack is empty again
    print(stack.is_empty())  # output: True
    print(stack.pop())
if __name__ == '__main__':
    main()
    
