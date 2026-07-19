from threading import Lock, Semaphore

class DiningPhilosophers:
    def __init__(self):
        self.forks = [Lock() for _ in range(5)]
        self.semaphore = Semaphore(4)

    def wantsToEat(
        self,
        philosopher: int,
        pickLeftFork,
        pickRightFork,
        eat,
        putLeftFork,
        putRightFork,
    ) -> None:

        left = philosopher
        right = (philosopher + 1) % 5

        self.semaphore.acquire()

        self.forks[left].acquire()
        self.forks[right].acquire()

        pickLeftFork()
        pickRightFork()
        eat()
        putRightFork()
        putLeftFork()

        self.forks[right].release()
        self.forks[left].release()

        self.semaphore.release()