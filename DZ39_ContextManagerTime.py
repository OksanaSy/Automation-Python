import time


class Timer:
    def __init__(self):
        self.start= time.perf_counter()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.elapsed_time = time.perf_counter() - self.start
        return self.elapsed_time

    def reset(self):
        self.start = time.perf_counter()
        return self

with Timer() as t:
  time.sleep(1)
print(t.elapsed_time) # ~1 second
time.sleep(2)
with t:
  time.sleep(5)
print(t.elapsed_time) # ~8 seconds
with Timer() as t2:
    time.sleep(1)
print(t2.elapsed_time)  # ~1 second
t2.reset()
with t2:
    time.sleep(2)
print(t2.elapsed_time)  # ~2 seconds
