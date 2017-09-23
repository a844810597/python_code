class Celcius:
    def __init__(self, value=26.0):
        print('Cel.__init__')
        self.value = float(value)

    def __get__(self, instance, owner):
        print('__Cel.get__')
        return self.value

    def __set__(self, instance, value):
        print('Cel.__set__')
        self.value = float(value)

class Fehrenheit:
    def __get__(self, instance, owner):
        print("Feh.__get__")
        return instance.cel * 1.8 + 32

    def __set__(self, instance, value):
        print("Feh.__set__")
        instance.cel = (float(value) - 32) / 1.8

class Temperature:
    cel = Celcius()
    feh = Fehrenheit()
