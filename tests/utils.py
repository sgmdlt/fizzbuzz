class FakePrompt():
    numbers = []

    def __init__(self, numbers):
        self.numbers = numbers[::-1]
    
    def get_number(self, *args):
        return self.numbers.pop()


class FakeOut():
    storage = []
    def write(self, *args):
        self.storage.extend(args)
