from threading import Semaphore

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fizz_sem = Semaphore(0)
        self.buzz_sem = Semaphore(0)
        self.fb_sem = Semaphore(0)
        self.num_sem = Semaphore(1)

    def release_next(self, x):
        if x > self.n:
            self.fizz_sem.release()
            self.buzz_sem.release()
            self.fb_sem.release()
            self.num_sem.release()
        elif x % 15 == 0:
            self.fb_sem.release()
        elif x % 3 == 0:
            self.fizz_sem.release()
        elif x % 5 == 0:
            self.buzz_sem.release()
        else:
            self.num_sem.release()

    def fizz(self, printFizz):
        for i in range(3, self.n + 1, 3):
            if i % 5 == 0:
                continue
            self.fizz_sem.acquire()
            printFizz()
            self.release_next(i + 1)

    def buzz(self, printBuzz):
        for i in range(5, self.n + 1, 5):
            if i % 3 == 0:
                continue
            self.buzz_sem.acquire()
            printBuzz()
            self.release_next(i + 1)

    def fizzbuzz(self, printFizzBuzz):
        for i in range(15, self.n + 1, 15):
            self.fb_sem.acquire()
            printFizzBuzz()
            self.release_next(i + 1)

    def number(self, printNumber):
        for i in range(1, self.n + 1):
            if i % 3 != 0 and i % 5 != 0:
                self.num_sem.acquire()
                printNumber(i)
                self.release_next(i + 1)