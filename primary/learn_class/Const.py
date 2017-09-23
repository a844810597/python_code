class Const:
    def __setattr__(self, name, value):
        if name != name.upper():
            raise TypeError('常量名必须为大写')

        if hasattr(self, name):
            raise TypeError('常量不可改变')

        super().__setattr__(name, value)

    '''
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise TypeError('常量不可改变')

        if hasattr(self, name):
            raise TypeError('常量不可改变')

        self.__dict__[name] = value
    '''

import sys
sys.modules[__name__] = Const()
