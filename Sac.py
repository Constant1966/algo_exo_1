class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Sac:
    def __init__(self):
        self.head = None

    def est_vide(self):
        return self.head is None

    def ajouter(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def iterer(self):
        current = self.head
        while current:
            yield current.value
            current = current.next


if __name__ == '__main__':
    s = Sac()
    el = [3, 1, 34, 1, 46, 7, 87, 6]
    for elem in el:
        s.ajouter(elem)

    print(s.est_vide())

