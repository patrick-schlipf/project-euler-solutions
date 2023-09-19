from com.patrick.private.utils.benchmark import Benchmark


class Problem(object):
    """
    Text
    """

    def __init__(self, param: int):
        self.param = param
        print(f"Problem XXX: {self.param}")
        print(f"param={self.param}")

    @Benchmark
    def attempt_1(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem(param="XXX")

    problem.attempt_1()
    problem.official_solution()
