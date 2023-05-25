import random
import waitqueue
import leito
import patient

#gerador de eventos para a simulação

def generateEvents(hospitais, time):
	event = random.randint(1,100)
	queue = waitqueue.waitqueue()
## chegada de leitos
	if 6 <= event <= 45: 

		nleitos = random.randint(1, 6)
		div = random.randint(1,3)
		nleitos = nleitos//div
		for i in range(nleitos):

# para diminuir as chances de uma ocorrência duplicada em um número de leito, primeiro fazemos um sorteio de um número de 7 a 159 e depois multiplicamos por um primo entre os que estão na lista, pois o produto de um número por um desses primos é único, em seguida fazemos o número mod 1000 para pegar os 3 últimos digitos.
			hospital = random.randint(1, hospitais)
			id_leito = random.randint(7, 159)
			aux = random.choice(['31', '29', '41', '47', '73'])
			id_leito = id_leito * int(aux)
			id_leito = id_leito%1000

			tipo = random.choice(['NEONATAL', 'PEDIATRICA', 'ADULTO'])

			uti = leito.leito(hospital, id_leito, tipo)
			queue.insert(uti)



## chegada de pacientes
	elif 46 <= event <= 100:

		npacientes = random.randint(1, 10)
		for i in range(npacientes):

# para os pacientes seguimos o mesmo princípio dos números primos, porém com maiores chances de sucesso, devido ao tamanho do número (esse maior cuidado com os pacientes é devido ao seu maior fluxo de entrada no programa)
			badge = random.randint(20,148327)
			aux = random.choice(['31', '29', '41', '47', '73'])
			badge = badge * int(aux)
			badge += random.randint(10000000, 80000000)

			tipo = random.choice(['NEONATAL', 'PEDIATRICA', 'ADULTO'])

			status = random.choice(['VERMELHO', 'LARANJA', 'AMARELO'])

			paciente = patient.patient(badge, tipo, status, time)
			queue.insert(paciente)

	return queue
