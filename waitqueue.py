# estrutura que cria filas de espera para as UTIs
import cNo

class waitqueue:

	def __init__(self):
		self.__size__ = 0
		self.__first__ = None
		self.__last__ = None

# função de inserção

	def insert(self, pearson):
		to_insert = cNo.cNo(pearson)
		if(self.__size__ > 0):
			self.__last__.setProx(to_insert)
			self.__last__ = to_insert
			self.__size__ += 1
			return

		self.__first__ = to_insert
		self.__last__ = to_insert
		self.__size__ += 1
		return

# função empty 

	def empty(self):
		if self.__size__ == 0 or self.__first__ is None:
			return True
		return False

# função pop

	def pop(self):
		if self.__size__ > 0:
			to_pop = self.__first__
			self.__first__ = to_pop.getProx()
			to_return = to_pop.getDado()
			del to_pop
			self.__size__ -= 1
			return to_return
		return False


# função print para a fila
	def __str__(self):
		outStr = ""
		if(self.__size__ > 0):
			curr = self.__first__
			while(self.__last__ != None):
				outStr += f"{curr.getBadge} | {curr.getAge} | {curr.getStatus} \n"
				curr = curr.getProx()
			return outStr
		outStr = "-------FILA VAZIA------"
		return outStr

# get first

	def getFirst(self):
		return self.__first__


# remove para remover paciente no meio de uma fila

	def remove(self, patient):
		if self.__first__.getDado().getBadge() == patient:
			curr = self.__first__
			self.__first__ = curr.getProx()

		else:
			ant = self.__first__
			curr = ant.getProx()

			while curr is not None:
				if curr.getDado().getBadge() == patient:
					ant.setProx(curr.getProx())
					break
				ant = curr
				curr = ant.getProx()

		del curr
		self.__size__ -= 1
		return

