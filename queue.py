from linked_list import LinkedList

class Queue(object):

    def __init__(self):
        self.data = LinkedList()

    def enqueue(self, data):
        self.data.insert_at_end(data)

    def dequeue(self):
        return self.data.remove_first()

    def peek(self):
        return self.data.peekLast()

    def get_size(self):
        return self.data.get_length()

    def traverse(self):
        self.data.traverse()


def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print('----------------')
    q.traverse()
    print('----------------')
    print(q.dequeue().data)
    print(q.dequeue().data)
    print('----------------')
    print(q.get_size())
    print('----------------')
    q.traverse()

if __name__ == '__main__':
    main()
