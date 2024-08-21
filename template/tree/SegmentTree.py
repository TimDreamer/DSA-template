class TreeNode:
    def __init__(self, start, end, val, left = None, right = None):
        self.start = start
        self.end = end
        self.val = val
        self.left = left
        self.right = right

class SegTree:
    def __init__(self, arr):
        self._arr = arr
        self.root = self._buildTree(0, len(self._arr) - 1)

    def _buildTree(self, start, end):
        if start == end:
            return TreeNode(start, end, self._arr[start])

        mid = (start + end) >> 1
        left = self._buildTree(start, mid)
        right = self._buildTree(mid + 1, end)
        return TreeNode(start, end, left.val + right.val, left, right)

    def _query(self, node, start, end):
        if start > end:
            return 0

        if node.start == start and node.end == end:
            return node.val

        mid = (node.start + node.end) >> 1

        return self._query(node.left, start, min(mid, end)) + self._query(node.right, max(mid + 1, start), end)

        # classic version
        # if end <= mid:
        #     return self._query(node.left, start, end)
        # if start > mid:
        #     return self._query(node.right, start, end)

        # return self._query(node.left, start, mid) + self._query(node.right, mid + 1, end)

    def _update(self, node, index, value):
        if node.start == node.end:
            if node.start == index:
                node.val = value
            return

        mid = (node.start + node.end) >> 1
        if index <= mid:
            self._update(node.left, index, value)
        else:
            self._update(node.right, index, value)

        node.val = node.left.val + node.right.val

    def query(self, start, end):
        return self._query(self.root, start, end)

    def update(self, index, value):
        return self._update(self.root, index, value)
