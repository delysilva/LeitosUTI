# estrutura que cria pilhas para armazenar os leitos
import cNo

class stack:

	def __init__(self):
		self.__size__ = 0
		self.__top__ = None

# função de inserção

	def insert(self, leito):
		to_insert = cNo.cNo(leito)
		if(self.__size__ > 0):
			to_insert.setProx(self.__top__)
			self.__top__ = to_insert
			self.__size__ += 1
			return

		self.__top__ = to_insert
		self.__size__ += 1
		return


# função get pro tamanho

	def empty(self):
		if self.__size__ == 0:
			return True
		return False

# função pop

	def pop(self):
		if self.__size__ != 0:
			to_pop = self.__top__
			self.__top__ = to_pop.getProx()
			data = to_pop.getDado()
			del to_pop
			self.__size__ -= 1
			return data
		return False

	def getTop(self):
		return self.__top__

	def size(self):
		return self.__size__


