#classe que cira objetos do tipo paciente. Os objetos possuem um ID único (badge), um tipo de UTI adequada para a sua idade (age), o seu estado de urgência (status), e o seu tempo de entrada no sistema (time)

import random
class patient:

	def __init__(self, badge, age, status, time):
		self.__badge__ = badge
		self.__age__ = age
		self.__status__ = status
		self.__enter__= time

	def __del__(self):
		del self
		return True

	def getEnter(self):
		return self.__enter__

	def setEnter(self, time):
		self.__enter__ = time
		return

	def getStatus(self):
		return self.__status__

	def getAge(self):
		return self.__age__

	def getBadge(self):
		return self.__badge__

# função que realiza sorteios para decidir se um paciente muda de status ou permanece o mesmo


	def changeStatus(self, tempo):

# quanto mais o tempo dele na fila aumenta, mais chances ele tem de piorar
		tempo = tempo - self.__enter__
		change = random.randint(1, 100)
		if self.__status__ == 'VERMELHO':

			if change <= 15 + tempo:
				self.__status__ = 'MORREU'
				return True

			elif 15 + tempo < change <= 85:
				return False

			elif change > 85:
				self.__status__ = 'LARANJA'
				return True


		elif self.__status__ == 'LARANJA':

			if change <= 10 + tempo:
				self.__status__ = 'VERMELHO'
				return True

			elif 10 + tempo < change <= 75:
				return False

			elif change > 75:
				self.__status__ = 'AMARELO'
				return True



		elif self.__status__ == 'AMARELO':

			if change <= 5 + tempo:
				self.__status__ = 'LARANJA'
				return True

			elif 5 + tempo < change <= 70:
				return False

			elif change > 70:
				self.__status__ = 'VERDE'
				return True


	def __str__(self):
		outStr = ""
		outStr += f"{self.__badge__} | {self.__age__} | self.__{status}"
		return outStr




		
