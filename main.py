import poolleitos
import waitroom
import patient
import leito
import sys
import time
import generateEvents

leitos = poolleitos.poolLeitos()
pacientes = waitroom.waitroom()
if len(sys.argv) <= 1:
	hospitais = 1
else:
	if int(sys.argv[1]) > 0:
		hospitais = int(sys.argv[1])
	else:
		hospitais = 1

if __name__ == '__main__':

# gerar pacientes ou leitos
	entrada = str(0)
	tempo = -1
	while hospitais > 0 and entrada not in "Qq":
		tempo += 1
		for i in range(5):
			to_do = generateEvents.generateEvents(hospitais, tempo)
			if not to_do.empty():
				if type(to_do.getFirst().getDado()) is leito.leito:
					while not to_do.empty():
						aux = to_do.pop()
						leitos.insert(aux)
				else:
					while not to_do.empty():
						aux = to_do.pop()
						pacientes.insert(aux)



# imprimir a situação inicial das filas de espera e dos leitos
		print(pacientes)
		print(leitos)

		time.sleep(2)


# atribuir leitos a pacientes
		if not leitos.emptyNeo():
			while not pacientes.emptyNeo() and not leitos.emptyNeo():
				pessoa = pacientes.popNeo()
				uti = leitos.popNeo()
				time.sleep(0.5)
				print(f"\033[35mPaciente portador do ID: {pessoa.getBadge()} | Precisando de UTI: {pessoa.getAge()} | Em situação: {pessoa.getStatus()}  ====== ENCAMINHADO PARA A UTI ===========>> No Hospital: {uti.getHospital()} | Identificador da UTI: {uti.getId()} | Tipo da UTI: {uti.getUTI()}\n")


		time.sleep(1)
		if not leitos.emptyPed():
			while not pacientes.emptyPed() and not leitos.emptyPed():
				pessoa = pacientes.popPed()
				uti = leitos.popPed()
				time.sleep(0.5)
				print(f"\033[35mPaciente portador do ID: {pessoa.getBadge()} | Precisando de UTI: {pessoa.getAge()} | Em situação: {pessoa.getStatus()}  ====== ENCAMINHADO PARA A UTI ===========>> No Hospital: {uti.getHospital()} | Identificador da UTI: {uti.getId()} | Tipo da UTI: {uti.getUTI()}\n")
		time.sleep(1)
		if not leitos.emptyAdu():
			while not pacientes.emptyAdu() and not leitos.emptyAdu():
				pessoa = pacientes.popAdu()
				uti = leitos.popAdu()
				time.sleep(0.5)
				print(f"\033[35mPaciente portador do ID: {pessoa.getBadge()} | Precisando de UTI: {pessoa.getAge()} | Em situação: {pessoa.getStatus()}  ====== ENCAMINHADO PARA A UTI ===========>> No Hospital: {uti.getHospital()} | Identificador da UTI: {uti.getId()} | Tipo da UTI: {uti.getUTI()}\n")

		pacientes.changeStatus(tempo)

		time.sleep(2)
		
		print(pacientes)
		print(leitos)
		entrada = str(input(f"\033[37mAtualmente a simulação está com {hospitais} hospital(is). Digite um número para somar ao número atual de hospitais (digite 'q' para parar a simulação ou '0' para continuar sem adicionar hospitais)\n"))
		if not entrada in "Qq":
			hospitais += int(entrada)



