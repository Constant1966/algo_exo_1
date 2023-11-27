class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class File:
    def __init__(self):
        self.front = None
        self.rear = None

    def est_vide(self):
        return self.front is None

    def enfiler(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def defiler(self):
        if self.est_vide():
            return None
        item = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return item

    def iterer(self):
        current = self.front
        while current:
            yield current.value
            current = current.next


if __name__ == '__main__':
    p = File()
    em = [3, 4, 5, 6, 7, 67]
    for i in em:
        p.enfiler(i)

    print(p.defiler())
    print(p.defiler())
    print(p.defiler())
