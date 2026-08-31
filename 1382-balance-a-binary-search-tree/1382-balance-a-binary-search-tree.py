class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            nodes.append(node)
            inorder(node.right)

        inorder(root)

        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            root = nodes[mid]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nodes) - 1)