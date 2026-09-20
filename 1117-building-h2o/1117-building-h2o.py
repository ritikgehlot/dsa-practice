from threading import Semaphore, Barrier

class H2O:
    def __init__(self):
        self.h = Semaphore(2)
        self.o = Semaphore(1)
        self.barrier = Barrier(3)

    def hydrogen(self, releaseHydrogen):
        self.h.acquire()
        releaseHydrogen()
        self.barrier.wait()

    def oxygen(self, releaseOxygen):
        self.o.acquire()
        releaseOxygen()
        self.barrier.wait()
        self.h.release()
        self.h.release()
        self.o.release()