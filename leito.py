class leito:

	def __init__(self, hospital, identificador, uti):
		self.__hospital__ = hospital
		self.__identificador__ = identificador
		self.__uti__ = uti

	def getHospital(self):
		return self.__hospital__

	def getId(self):
		return self.__identificador__

	def getUTI(self):
		return self.__uti__

