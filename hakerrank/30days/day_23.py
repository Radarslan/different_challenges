import sys
from queue import Queue


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        # Write your code here
        if root is not None:
            q = Queue()
            q.put(root)
            while not q.empty():
                tree = q.get()
                print(tree.data, end=" ")
                if tree.left is not None:
                    q.put(tree.left)

                if tree.right is not None:
                    q.put(tree.right)




a = [3, 5, 4, 7, 2, 1]
# T = int(input())
myTree = Solution()
root = None
# for i in range(T):
#     data = int(input())
for data in a:
    root = myTree.insert(root, data)
myTree.levelOrder(root)
