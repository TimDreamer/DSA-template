class BIT:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & (-index)

    def query(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & (-index)
        return total
