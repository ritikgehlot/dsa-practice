class TreeAncestor:

    def __init__(self, n: int, parent: list[int]):
        LOG = n.bit_length()
        self.up = [[-1] * LOG for _ in range(n)]

        for i in range(n):
            self.up[i][0] = parent[i]

        for j in range(1, LOG):
            for i in range(n):
                prev = self.up[i][j - 1]
                if prev != -1:
                    self.up[i][j] = self.up[prev][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        bit = 0

        while k > 0 and node != -1:
            if k & 1:
                node = self.up[node][bit]

            k >>= 1
            bit += 1

        return node