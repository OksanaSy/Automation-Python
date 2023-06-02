import time


class Timer:
    def __init__(self):
        self.elapsed_time = 0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        self.current = time.perf_counter() - self.start
        self.elapsed_time =self.elapsed_time+self.current
        return self.elapsed_time

    def reset(self):
        self.elapsed_time = 0
        return self


with Timer() as t:
    time.sleep(1)
print(t.elapsed_time)  # ~1 second
time.sleep(2)
with t:
    time.sleep(5)
print(t.elapsed_time)  # ~6 seconds
with t:
    time.sleep(10)
print(t.elapsed_time)
with Timer() as t2:
    time.sleep(1)
print(t2.elapsed_time)  # ~1 second
t2.reset()
print("reseted")
with t2:
    time.sleep(2)
print(t2.elapsed_time)  # ~2 seconds
with t2:
    time.sleep(4)
print(t2.elapsed_time)  # ~6 seconds
