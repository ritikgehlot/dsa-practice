class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx = {v: i for i, v in enumerate(inorder)}

        def build(l, r):
            if l > r:
                return None

            root = TreeNode(postorder.pop())
            mid = idx[root.val]

            root.right = build(mid + 1, r)
            root.left = build(l, mid - 1)

            return root

        return build(0, len(inorder) - 1)