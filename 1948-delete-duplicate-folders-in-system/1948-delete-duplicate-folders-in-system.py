from collections import defaultdict

class Node:
    def __init__(self):
        self.children = {}
        self.deleted = False


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Node()
        groups = defaultdict(list)

        # Build Trie
        for path in paths:
            node = root
            for name in path:
                if name not in node.children:
                    node.children[name] = Node()
                node = node.children[name]

        # Serialize subtrees
        def encode(node):
            if not node.children:
                return "()"

            parts = []

            for name in sorted(node.children):
                parts.append(
                    name + encode(node.children[name])
                )

            key = "(" + "".join(parts) + ")"
            groups[key].append(node)

            return key

        encode(root)

        # Mark duplicate folders
        for key, nodes in groups.items():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True

        # Build answer
        ans = []

        def dfs(node, path):
            for name, child in node.children.items():
                if child.deleted:
                    continue

                new_path = path + [name]
                ans.append(new_path)
                dfs(child, new_path)

        dfs(root, [])

        return ans