class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)

        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        ans = [1] * n
        previous = [-1] * n
        last = {}
        stack = [0]

        while stack:
            node = stack.pop()

            if node >= 0:
                previous[node] = last.get(s[node], -1)
                last[s[node]] = node

                stack.append(~node)
                stack.extend(children[node])

            else:
                node = ~node

                last[s[node]] = previous[node]

                new_parent = (
                    previous[node]
                    if previous[node] != -1
                    else parent[node]
                )

                if new_parent != -1:
                    ans[new_parent] += ans[node]

        return ans