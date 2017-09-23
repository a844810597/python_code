class Ticket:
	__expense = 100
	__increase = 1
	__discont = 1
	def __init__(self, weekends=False, child=False):
		if weekends:
			self.__increase = 1.2
		if child:
			self.__discont = 0.5
		self.price = self.__expense * self.__increase * self.__discont
	def getPrice(self):
		return print(self.price)
