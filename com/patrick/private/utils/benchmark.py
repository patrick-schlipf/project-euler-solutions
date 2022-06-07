import time
from functools import partial


class Benchmark(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("-" * 50)
        print(f"Execute method: {self.func.__name__}()")
        start = time.perf_counter_ns()

        # ---
        ret = self.func(*args, **kwargs)
        # ---

        end = time.perf_counter_ns()
        print(f"Took: {end - start} ns")
        print()

        return ret

    def __get__(self, instance, owner):
        return partial(self, instance)
