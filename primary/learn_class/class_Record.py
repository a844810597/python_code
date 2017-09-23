import time

class Record:
    def __init__(self, initval=None, name=None):
        self.name = name
        self.value = initval
        self.filename = 'record.txt'

    def __get__(self, instance, owner):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write('%s 变量于 %s 被访问，%s = %s\n' % \
                    (self.name, time.ctime(), self.name, str(self.value)))
        return self.value

    def __set__(self, instance, value):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write('%s 变量于 %s 被修改，%s --> %s\n' % \
                    (self.name, time.ctime(), str(self.value), str(value)))
        self.value = value

        
