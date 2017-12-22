#!/usr/bin/python3

import sys
import threading


sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)   # new thread will get stack of such size


def IsBinarySearchTree(tree, index=0):
    # Implement correct algorithm here
    # tree = [[1,1,2], [2,-1,-1], [3,-1-1]]
    if index == -1 or tree == []:
        return True

    key = tree[index][0]
    left_index = tree[index][1]
    right_index = tree[index][2]

    if (left_index != -1 and key < tree[left_index][0]) \
            or (right_index != -1 and key > tree[right_index][0]):
        return False

    return IsBinarySearchTree(tree, left_index) and IsBinarySearchTree(tree, right_index)


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
