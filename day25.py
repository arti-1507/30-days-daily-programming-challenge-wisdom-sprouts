import sys
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(arr):
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    q = collections.deque([root])
    i = 1

    while q and i < len(arr):
        node = q.popleft()

        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1

    return root


def isValidBST(root):
    def helper(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)

    return helper(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    raw = sys.stdin.read().strip()
    raw = raw.strip("[]").replace(" ", "").split(",")
    arr = [int(x) if x != "null" else None for x in raw]

    root = buildTree(arr)
    print("true" if isValidBST(root) else "false")
