# python3

import sys
import threading


sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Tree:
    def __init__(self, key, parent, children=None):
        self.key = key
        self.parent = parent
        self.children = children or []

    def get(self, key):
        if self.key == key:
            return self

        if len(self.children) == 0:
            return None

        for child in self.children:
            t = child.get(key)
            if t is not None:
                return t

    def height(self):
        if len(self.children) == 0:
            return 1
        heights = []
        for c in self.children:
            heights.append(c.height())
        return 1 + max(heights)


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.root_tree = None

        for i, p in enumerate(self.parent):
            self.insert(i, p)

    def insert(self, pos, parent_pos):
        if self.root_tree:
            t = self.root_tree.get(pos)
            if t is not None:
                return t

        if parent_pos == -1:
            self.root_tree = Tree(pos, None)
            return self.root_tree

        parent = self.insert(parent_pos, self.parent[parent_pos])
        t = Tree(pos, parent)
        parent.children.append(t)
        return t

    def compute_height(self):
        # Replace this code with a faster implementation
        return self.root_tree.height()


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()
