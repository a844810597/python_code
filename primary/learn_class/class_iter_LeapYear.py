class LeapYear:
    def __init__(self, begin=1900, end=2017):
        self.begin = begin
        self.end = end
        self.now = begin
        
    def __iter__(self):
        return self

    def isleap(self, year):
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return True
        else:
            return False

    def __next__(self):
        if self.begin <= self.now <= self.end:
            while not self.isleap(self.now):
                self.now += 1
            temp = self.now
            self.now += 1
            return temp
        else:
            raise StopIteration
