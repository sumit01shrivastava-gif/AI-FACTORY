import time


class Benchmarker:

    def benchmark(
        self,
        function,
    ):

        start = time.time()

        function()

        end = time.time()

        return {
            "duration": end - start,
        }
