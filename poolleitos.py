# Estrutura responsável por armazenar as pilhas de leitos


import stack

class poolLeitos:

	def __init__(self):
		self.__neonatal__ = stack.stack()
		self.__pediatrica__ = stack.stack()
		self.__adulto__ = stack.stack()

##################################################################################################################################################################
	def emptyNeo(self):
		if self.__neonatal__.empty():
			return True
		return False

#--------------------------------------------------------------------------------------------------------------------------------------------#
	def emptyPed(self):
		if self.__pediatrica__.empty():
			return True
		return False

#--------------------------------------------------------------------------------------------------------------------------------------------#
	def emptyAdu(self):
		if self.__adulto__.empty():
			return True
		return False


################################################################################################################################################################
	def insert(self, leito):

		if leito.getUTI() == "NEONATAL":
			self.__neonatal__.insert(leito)

		if leito.getUTI() == "PEDIATRICA":
			self.__pediatrica__.insert(leito)

		if leito.getUTI() == "ADULTO":
			self.__adulto__.insert(leito)

###############################################################################################################################################################
	def __str__(self):
		outstr = ""
		outstr += "\n"
		outstr += "\033[37m                            LEITOS                              \n"
		outstr += "\n"
		outstr += "\033[36m========================== NEONATAL ============================\n"
		outstr += "\n"
		curr = self.__neonatal__.getTop()
		if curr is None:
			outstr += "\033[36m                         PILHA VAZIA                           \n"
		while curr is not None:
			outstr += f'Hospital: {curr.getDado().getHospital()} | Leito: {curr.getDado().getId()} | Tipo: {curr.getDado().getUTI()} \n'
			curr = curr.getProx()

		
		outstr += "\n"


#--------------------------------------------------------------------------------------------------------------------------------------------#
		outstr += "\n"
		outstr += "\033[34m========================= PEDIÁTRICO ===========================\n"
		outstr += "\n"
		curr = self.__pediatrica__.getTop()
		if curr is None:
			outstr += "\033[34m                         PILHA VAZIA                           \n"
		while curr is not None:
			outstr += f'Hospital: {curr.getDado().getHospital()} | Leito: {curr.getDado().getId()} | Tipo: {curr.getDado().getUTI()} \n'
			curr = curr.getProx()

		
		outstr += "\n"
		
#--------------------------------------------------------------------------------------------------------------------------------------------#
		outstr += "\n"
		outstr += "\033[32m========================== ADULTO ==============================\n"
		outstr += "\n"
		curr = self.__adulto__.getTop()
		if curr is None:
			outstr += "\033[32m                         PILHA VAZIA                           \n"
		while curr is not None:
			outstr += f'Hospital: {curr.getDado().getHospital()} | Leito: {curr.getDado().getId()} | Tipo: {curr.getDado().getUTI()} \n'
			curr = curr.getProx()

		
		outstr += "\n"
		outstr += 150*"\033[30m#"





		return outstr

####################################################################################################################################

	def popNeo(self):
		return self.__neonatal__.pop()

#--------------------------------------------------------------------------------------------------------------------------------------------#
	def popPed(self):
		return self.__pediatrica__.pop()

#--------------------------------------------------------------------------------------------------------------------------------------------#
	def popAdu(self):
		return self.__adulto__.pop()

#####################################################################################################################################


#	def find(self, Id, hospital):


#		curr = self.__neonatal__.top()
#		while curr is not None:
#			if curr.getDado().getHospital() == hospital and curr.getDado().getId() == Id:
#				return False

#		curr = self.__pediatrica__.top()
#		while curr is not None:
#			if curr.getDado().getHospital() == hospital and curr.getDado().getId() == Id:
#				return False

#		curr = self.__adulto__.top()
#		while curr is not None:
#			if curr.getDado().getHospital() == hospital and curr.getDado().getId() == Id:
#				return False


#		return True
























