"""
- Python uses only one constructor method - __init__()
- Use @classmethod to create alternative class constructors
"""

class InputData:
    def read(self):
        raise NotImplementedError


class PathInputData(InputData):

    def __init__(self, path) -> None:
        super().__init__()
        self.path = path

    def read(self):
        with open(self.path) as f:
            return f.read()


class Worker:
    """Another example of abstract class"""
    def __init__(self, input_data) -> None:
        super().__init__()
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


class LineCounterWorker(Worker):

    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result