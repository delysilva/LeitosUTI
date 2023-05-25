# essa estrutura cria 3 "salas de espera" e cada "sala de espera" possui 3 filas que armazenam pacientes. A sala determina o tipo de UTI e as filas são identificadas seguindo a gravidade de cada caso.
import time
import room

class waitroom:

	def __init__(self):
		self.__neonatal__ = room.room()
		self.__pediatrica__ = room.room()
		self.__adulto__ = room.room()

	def __str__(self):
		outstr = ""
		outstr += 150*"\033[30m#"
		outstr += "\n"
		outstr += "\033[37m                           PACIENTES                            \n"
		outstr += "\n"
		outstr += "\033[36m==========================  NEONATAL ===========================\n"
		outstr += "\n"

		outstr += "\033[31m---------------------------EMERGÊNCIA---------------------------\n"
		curr = self.__neonatal__.getRed().getFirst()
		if curr is None:
			outstr += "                           FILA VAZIA                           \n"
		while curr is not None:

			outstr += f' Paciente: {curr.getDado().getBadge()} | Idade: {curr.getDado().getAge()} | Situação: {curr.getDado().getStatus()}\n'
			curr = curr.getProx()



		outstr += "\n"
		outstr += "\033[33m--------------------------MUITO URGENTE-------------------------\n"
		curr = self.__neonatal__.getOrange().getFirst()
		if curr is None:
			outstr += "                           FILA VAZIA                           \n"
		while curr is not None:

			outstr += f' Paciente: {curr.getDado().getBadge()} | Idade: {curr.getDado().getAge()} | Situação: {curr.getDado().getStatus()}\n'
			curr = curr.getProx()



		outstr += "\n"
		outstr += "\033[35m-----------------------------URGENTE----------------------------\n"
		curr = self.__neonatal__.getYellow().getFirst()
		if curr is None:
			outstr += "                           FILA VAZIA                           \n"
		while curr is not None:

			outstr += f' Paciente: {curr.getDado().getBadge()} | Idade: {curr.getDado().getAge()} | Situação: {curr.getDado().getStatus()}\n'
			curr = curr.getProx()
		outstr += "\n"


############################################################################################################################################################################

		outstr += "\n"
		outstr += "\033[34m=========================  PEDIÁTRICA ===========================\n"
		outstr += "\n"

		outstr += "\033[31m---------------------------EMERGÊNCIA---------------------------\n"
		curr = self.__pediatrica__.getRed().getFirst()
		if curr is None:
			outstr += "                           FILA VAZIA                           \n"
		while curr is not None:

			outstr += f' Paciente: {curr.getDado().getBadge()} | Idade: {curr.getDado().getAge()} | Situação: {curr.getDado().getStatus()}\n'
			curr = curr.getProx()

		

		outstr += "\n"
		outstr += "\033[33m--------------------------MUITO URGENTE-------------------------\n"
		curr = self.__pediatrica__.getOrange().getFirst()
		if curr is None:
			outstr += "                           FILA VAZIA                           \n"
		while curr is not None:

			outstr += f' Paciente: {curr.getDado().getBadge()} | Idade: {curr.getDado().getAge()} | Situação: {curr.getDado().getStatus()}\n'
			curr = curr.getProx()



		outstr += "\n"
		outstr += "\033[35m-----------------------------URGENTE----------------------------\n"
		curr = self.__pediatrica__.getYellow().getFirst()
		if curr is None:
			outstr += "                           FILA VAZIA                           \n"
		while curr is not None:

			outstr += f' Paciente: {curr.getDado().getBadge()} | Idade: {curr.getDado().getAge()} | Situação {curr.getDado().getStatus()}\n'
			curr = curr.getProx()


#########################################################################################################################################################################



		outstr += "\n"
		outstr += "\033[32m===========================  ADULTO ============================\n"
		outstr += "\n"
		outstr += "\033[31m---------------------------EMERGÊNCIA---------------------------\n"
		curr = self.__adulto__.getRed().getFirst()
		if curr is None:
			outstr += "                           FILA VAZIA                           \n"
		while curr is not None:

			outstr += f' Paciente: {curr.getDado().getBadge()} | Idade: {curr.getDado().getAge()} | Situação: {curr.getDado().getStatus()}\n'
			curr = curr.getProx()

		

		outstr += "\n"
		outstr += "\033[33m--------------------------MUITO URGENTE-------------------------\n"
		curr = self.__adulto__.getOrange().getFirst()
		if curr is None:
			outstr += "                           FILA VAZIA                           \n"
		while curr is not None:

			outstr += f' Paciente: {curr.getDado().getBadge()} | Idade: {curr.getDado().getAge()} | Situação: {curr.getDado().getStatus()}\n'
			curr = curr.getProx()




		outstr += "\n"
		outstr += "\033[35m-----------------------------URGENTE----------------------------\n"
		curr = self.__adulto__.getYellow().getFirst()
		if curr is None:
			outstr += "                           FILA VAZIA                           \n"
		while curr is not None:

			outstr += f' Paciente: {curr.getDado().getBadge()} | Idade: {curr.getDado().getAge()} | Situação: {curr.getDado().getStatus()}\n'
			curr = curr.getProx()
		outstr += "\n"
		outstr += 150*"\033[30m#"


		return outstr

########################################################################################################################################################################
# inserir um paciente

	def insert(self, patient):
		if patient.getAge() == "NEONATAL":
			self.__neonatal__.insert(patient)
		elif patient.getAge() == "PEDIATRICA":
			self.__pediatrica__.insert(patient)
		elif patient.getAge() == "ADULTO":
			self.__adulto__.insert(patient)
		return

########################################################################################################################################################################
# consultar se a fila específica está vazia

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

########################################################################################################################################################################
# pop de uma fila específica

	def popNeo(self):
		return self.__neonatal__.pop()

#--------------------------------------------------------------------------------------------------------------------------------------------#
	def popPed(self):
		return self.__pediatrica__.pop()

#--------------------------------------------------------------------------------------------------------------------------------------------#
	def popAdu(self):
		return self.__adulto__.pop()


########################################################################################################################################################################
# função que muda ou não o status do paciente

	def changeStatus(self, tempo):

		self.__neonatal__.changeStatus(tempo)
		self.__pediatrica__.changeStatus(tempo)
		self.__adulto__.changeStatus(tempo)
		return
