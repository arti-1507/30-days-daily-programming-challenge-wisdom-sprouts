class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    return left if left else right


def build_tree(values):
    if not values or values[0] == "null":
        return None

    nodes = [TreeNode(int(values[0]))]
    root = nodes[0]
    i = 1
    for node in nodes:
        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            nodes.append(node.left)
        i += 1
        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            nodes.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    values = input().strip().split()
    p_val = int(input().strip())
    q_val = int(input().strip())

    root = build_tree(values)

    def find_node(root, val):
        if not root:
            return None
        if root.val == val:
            return root
        return find_node(root.left, val) or find_node(root.right, val)

    p = find_node(root, p_val)
    q = find_node(root, q_val)

    lca = lowestCommonAncestor(root, p, q)
    print(lca.val)
