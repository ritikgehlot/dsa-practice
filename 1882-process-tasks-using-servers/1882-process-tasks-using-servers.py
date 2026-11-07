class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []

        time = 0

        for i, duration in enumerate(tasks):
            time = max(time, i)

            # Release servers whose tasks have finished
            while busy and busy[0][0] <= time:
                finish, weight, server = heapq.heappop(busy)
                heapq.heappush(available, (weight, server))

            # If no server is available, wait for the next one
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    finish, weight, server = heapq.heappop(busy)
                    heapq.heappush(available, (weight, server))

            # Choose the server with minimum weight, then minimum index
            weight, server = heapq.heappop(available)

            ans.append(server)

            heapq.heappush(
                busy,
                (time + duration, weight, server)
            )

        return ans