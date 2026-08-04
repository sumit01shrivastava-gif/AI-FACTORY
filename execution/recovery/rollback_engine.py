import shutil


class RollbackEngine:

    def rollback(self, source, destination):
        shutil.copytree(source, destination)
