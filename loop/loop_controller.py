import time


class LoopController:

    def __init__(self):

        self.running = False

    def start(self):

        self.running = True

    def stop(self):

        self.running = False

    def cycle(
        self,
        function,
    ):

        while self.running:

            function()

            time.sleep(1)
