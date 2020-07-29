class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return bool(len(self.elements) == 0)

    def push(self, item):
        if self.is_empty():
            self.elements.append(item)
        else:
            i = 0
            contains = False

            while not contains and i < len(self.elements):
                if item.f_cost < self.elements[i].f_cost:
                    self.elements.insert(i, item)
                    contains = True
                else:
                    i += 1
            if not contains:
                self.elements.append(item)

    def pop(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.elements.pop(0)

    def pop_last(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.elements.pop(len(self.elements) - 1)
