import time


class Timer:
    def __enter__(self):
        self.elapsed_time = time.perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        self.elapsed_time = time.perf_counter() - self.elapsed_time
        return self.elapsed_time

    def reset(self):
        self.elapsed_time = time.perf_counter()
        return self


with Timer() as t:
    time.sleep(1)
print(t.elapsed_time)  # ~1 second
time.sleep(1)
with t:
    time.sleep(5)
print(t.elapsed_time)  # ~5 seconds

with Timer() as t2:
    time.sleep(3)
print(t2.elapsed_time)  # ~3 second
t2.reset()
with t2:
    time.sleep(1)
print(t2.elapsed_time)  # ~1 seconds