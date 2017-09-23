class MyRev:
    def __init__(self, content):
        self.content = content
        self.index = len(content) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            temp = self.index
            self.index -= 1
            return self.content[temp]
        else:
            raise StopIteration
    
