
class Stack(object):

    def __init__(self):
        self._stack = []

    def push(self, data):
        self._stack.append(data)

    def pop(self):
        item = self._stack[-1]
        del self._stack[-1]
        return item

    def peek(self):
        return self._stack[-1]

    def get_size(self):
        return len(self._stack)


def main():
    stack = Stack()
    stack.push(1)
    stack.push(33)
    print(stack.get_size())
    print(stack.peek())
    print(stack.get_size())
    stack.pop()
    print(stack.get_size())



if __name__ == '__main__':
    main()