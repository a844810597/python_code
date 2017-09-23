import os
import pickle

class MyDes:
    saved = []

    def __init__(self, attrname=None):
        self.attrname = attrname
        self.filename = attrname + '.pkl'

    def __get__(self, instance, owner):
        if self.attrname not in MyDes.saved:
            raise AttributeError('%s 属性还没有赋值！' % self.attrname)
        else:
            with open(self.filename, 'rb') as pickle_file:
                value = pickle.load(pickle_file)
            return value

    def __set__(self, instance, value):
        with open(self.filename, 'wb') as pickle_file:
            pickle.dump(value, pickle_file)
        MyDes.saved.append(self.attrname)

    def __delete__(self, instance):
        os.remove(self.filename)
        MyDes.saved.remove(self.attrname)
