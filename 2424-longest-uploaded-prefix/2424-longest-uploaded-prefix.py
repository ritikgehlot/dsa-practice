class LUPrefix:

    def __init__(self, n: int):
        self.uploaded = [False] * (n + 2)
        self.longest_uploaded = 0

    def upload(self, video: int) -> None:
        self.uploaded[video] = True

    def longest(self) -> int:
        while self.uploaded[self.longest_uploaded + 1]:
            self.longest_uploaded += 1
        return self.longest_uploaded