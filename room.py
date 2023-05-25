# essa classe tem 3 atributos que são 3 filas de espera, uma para cada gravidade

import patient
import waitqueue
import time


class room:

	def __init__(self):
		self.__RED__ = waitqueue.waitqueue()
		self.__ORANGE__ = waitqueue.waitqueue()
		self.__YELLOW__ = waitqueue.waitqueue()

	def getRed(self):
		return self.__RED__

	def getOrange(self):
		return self.__ORANGE__

	def getYellow(self):
		return self.__YELLOW__



	def insert(self, n):
		code = n.getStatus()
		if code == "VERMELHO":
			self.__RED__.insert(n)

		if code == "LARANJA":
			self.__ORANGE__.insert(n)

		if code == "AMARELO":
			self.__YELLOW__.insert(n)

		return


	def pop(self):
		if(not self.__RED__.empty()):
			return self.__RED__.pop()	

		elif(not self.__ORANGE__.empty()):
			return self.__ORANGE__.pop()

		elif(not self.__YELLOW__.empty()):
			return self.__YELLOW__.pop()
		
		return


	def empty(self):
		if(self.__RED__.empty() and self.__ORANGE__.empty() and self.__YELLOW__.empty()):
			return True
		return False

######################################################################################################################
# função que percorre os pacientes para sortear a mudança de estado
	def changeStatus(self, tempo):

		ans = waitqueue.waitqueue()

#rodar para os casos de emergência

		if not self.__RED__.empty():
			curr = self.__RED__.getFirst()
			while curr is not None:
				if curr.getDado().changeStatus(tempo):
					self.__RED__.remove(curr.getDado().getBadge())

					if curr.getDado().getStatus() == "MORREU":
						print(f"\033[31mO paciente: {curr.getDado().getBadge()} | Da fila para UTI's {curr.getDado().getAge()} | Em situação: EMERGÊNCIA | Entrada: {curr.getDado().getEnter()} | ===== PIOROU DE CONDIÇÃO =====> Infelizmente, o paciente faleceu. Hora da morte {tempo}. \n")
						ans.insert(curr.getDado())


					elif curr.getDado().getStatus() == "LARANJA":
						print(f"\033[32mO paciente: {curr.getDado().getBadge()} | Da fila para UTI's {curr.getDado().getAge()} | Em situação: EMERGÊNCIA | Entrada: {curr.getDado().getEnter()} | ===== MELHOROU DE CONDIÇÃO =====> Agora está com caso considerado MUITO URGENTE. \n")
						ans.insert(curr.getDado())

				curr = curr.getProx()
				

# rodar para todos os casos muito urgentes

		elif not self.__ORANGE__.empty():
			curr = self.__ORANGE__.getFirst()

			while curr is not None:
				if curr.getDado().changeStatus(tempo):
					self.__ORANGE__.remove(curr.getDado().getBadge())

					if curr.getDado().getStatus() == "VERMELHO":
						print(f"\033[31mO paciente: {curr.getDado().getBadge()} | Da fila para UTI's {curr.getDado().getAge()} | Em situação: MUITO URGENTE | Entrada: {curr.getDado().getEnter()} | ===== PIOROU DE CONDIÇÃO =====> Agora está em estado de EMERGÊNCIA. \n")
						ans.insert(curr.getDado())


					elif curr.getDado().getStatus() == "AMARELO":
						print(f"\033[32mO paciente: {curr.getDado().getBadge()} | Da fila para UTI's {curr.getDado().getAge()} | Em situação: MUITO URGENTE | Entrada: {curr.getDado().getEnter()} | ===== MELHOROU DE CONDIÇÃO =====> Agora está com caso considerado URGENTE. \n")
						ans.insert(curr.getDado())

				curr = curr.getProx()



# rodar para todos os casos urgentes
		elif not self.__YELLOW__.empty():
			curr = self.__YELLOW__.getFirst()
			while curr is not None:
				if curr.getDado().changeStatus(tempo):
					self.__YELLOW__.remove(curr.getDado().getBadge())

					if curr.getDado().getStatus() == "LARANJA":
						print(f"\033[31mO paciente: {curr.getDado().getBadge()} | Da fila para UTI's {curr.getDado().getAge()} | Em situação: URGENTE | Entrada: {curr.getDado().getEnter()} | ===== PIOROU DE CONDIÇÃO =====> Agora está com caso considerado MUITO URGENTE. \n")
						ans.insert(curr.getDado())


					elif curr.getDado().getStatus() == "VERDE":
						print(f"\033[32mO paciente: {curr.getDado().getBadge()} | Da fila para UTI's {curr.getDado().getAge()} | Em situação: URGENTE | Entrada: {curr.getDado().getEnter()} | ===== MELHOROU DE CONDIÇÃO =====> Agora está com caso considerado POUCO URGENTE. \n")
						ans.insert(curr.getDado())
				curr = curr.getProx()



# colocar os caras que mudaram de estado nas novas filas:
		while not ans.empty():
			aux = ans.pop()
			if aux.getStatus() == "VERMELHO":
				self.__RED__.insert(aux)
			elif aux.getStatus() == "LARANJA":
				self.__ORANGE__.insert(aux)
			elif aux.getStatus() == "AMARELO":
				self.__YELLOW__.insert(aux)
			else:
				del aux

		return



###################################################################################################


		







				
