from threading import Thread, Event, Lock
import time

A_READY = Event()
STDOUT_LOCK = Lock()

def pr(*args):
    with STDOUT_LOCK:
        print(*args, end='', flush=True)

def divisible_by_n(value, n):
    if value == 0:
        return True
    if (value > 0) and ((value % n) == 0):
        return True
    return False

class ThreadA(Thread):

    def run(self):
        for i in range(1, 50):
            pr(f"A{i}")
            if divisible_by_n(i, 10):
                A_READY.set()  # notify b
                pr("/setting/")
            elif divisible_by_n(i, 5):
                A_READY.clear()  # stop notifying b
                pr("/clearing/")
            time.sleep(.1)
        pr("/setting/")
        A_READY.set()  # notify b and let b finish


class ThreadB(Thread):

    def run(self):
        for i in range(1, 50):
            A_READY.wait()  # wait until event is set by ThreadA
            pr(f"B{i}")
            time.sleep(.1)


t_a = ThreadA()
t_a.start()
t_b = ThreadB()
t_b.start()
t_a.join()
t_b.join()
print()
