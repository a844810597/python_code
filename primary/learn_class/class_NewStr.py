class NewStr(str):
    def __sub__(self, other):
        return self.replace(other, '')

    def __lshift__(self, value):
        return NewStr(self[value : ] + self[ : value])

    def __rshift__(self, value):
        return NewStr(self[-value : ] + self[ : -value])
        
