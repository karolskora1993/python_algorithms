
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, data):
        node = Node(data)  
        if self.head:
            node.next = self.head
        self.head = node
        self.length += 1

    def insert_at_end(self, data):
        node =  Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node
        self.length += 1

    def remove_first(self):
        to_return = self.head
        if self.head:
            self.head = self.head.next
        else:
            self.head = None
        self.length -= 1
        return to_return

    def remove_last(self):
        current = self.head
        while current.next.next:
            current = current.next
        to_return  = current.next
        current.next = None
        self.length -= 1
        return to_return

    def remove(self, data):
        current = self.head
        prev = None
        while current.next:
            if current.data == data:
                if prev and prev.next:
                    prev.next = current.next
                else:
                    self.head = None
                self.length -= 1
                return current
            prev = current
            current = current.next
        print('item not found')
        return None

    def get_length(self):
        return self.length  

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def peekLast(self):
        current = self.head
        while current.next:
            current = current.next
        return current


def main():
    list = LinkedList()
    list.insert_at_beginning(1)
    list.insert_at_beginning(0)
    list.insert_at_end(2)
    list.insert_at_end(3)
    list.insert_at_end(4)
    list.insert_at_end(5)
    print(list.traverse())
    list.remove_first()
    print(list.traverse())
    list.remove_last()
    print(list.traverse())
    list.insert_at_end(44)
    list.insert_at_end(55)
    list.insert_at_end(66)
    list.insert_at_end(77)
    list.remove(66)
    print(list.traverse())
    print(list.get_length())


if __name__ == '__main__':
    main()
