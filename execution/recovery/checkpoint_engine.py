import shutil


class CheckpointEngine:

    def create(self, source, destination):
        shutil.copytree(source, destination)

