#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size

nodes = int(sys.stdin.readline().strip())
tree = []
keys = []
left_indexes = []
right_indexes = []

for i in range(nodes):
    k, l, r = map(int, sys.stdin.readline().strip().split())
    keys.append(k)
    left_indexes.append(l)
    right_indexes.append(r)

max_values = [None] * len(keys)
min_values = [None] * len(keys)


def RemoveNone(l):
    return [i for i in l if i is not None]


def GetMax(index=0):
    if index == -1:
        return None
    l = RemoveNone([keys[index], GetMax(left_indexes[index]), GetMax(right_indexes[index])])
    max_values[index] = max(l)
    return max_values[index]

def GetMin(index=0):
    if index == -1:
        return None
    l = RemoveNone([keys[index], GetMin(left_indexes[index]), GetMin(right_indexes[index])])
    min_values[index] = min(l)
    return min_values[index]


def IsBinarySearchTree(index=0):
    # Implement correct algorithm here
    # tree = [[1,1,2], [2,-1,-1], [3,-1-1]]
    if index == -1:
        return True

    k = keys[index]
    l = left_indexes[index]
    r = right_indexes[index]
    if (l != -1 and max_values[l] >= k) or (r != -1 and min_values[r] <= k):
        return False
    return IsBinarySearchTree(l) and IsBinarySearchTree(r)


def main():
    if nodes == 0:
        print("CORRECT")
        return
    GetMax(0)
    GetMin(0)
    if IsBinarySearchTree():
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
