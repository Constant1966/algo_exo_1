class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Pile:
    def __init__(self):
        self.top = None

    def est_vide(self):
        return self.top is None

    def empiler(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def depiler(self):
        if self.est_vide():
            return None
        item = self.top.value
        self.top = self.top.next
        return item

    def element_de_tete(self):
        if self.est_vide():
            return None
        return self.top.value

    def iterer(self):
        current = self.top
        while current:
            yield current.value
            current = current.next


if __name__ == '__main__':
    em = Pile()
    elements = [3, 1, 34, 1, 46, 7, 87, 6]
    for element in elements:
        em.empiler(element)

    print(em.element_de_tete())
    print(em.depiler())
    print(em.depiler())
    print(em.depiler())

