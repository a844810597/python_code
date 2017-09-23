class MyDes:
    def __init__(self, initval=None, name=None):
        self.value = initval
        self.name = name

    def __get__(self, instance, owner):
        print('正在访问变量：', self.name)
        return self.value
    
    def __set__(self, instance, value):
        print('正在设置变量：', self.name)
        self.value = value

    def __delete__(self, instance):
        print('正在删除变量：', self.name)
