def calculaPesos(grafo):

	'''Responsável por calcular o peso das arestas quando há e quando não há pesos'''


	try:
		pesoTotal = sum(grafo.es['weight'])
	except:
		pesoTotal = grafo.ecount()


	return pesoTotal

def modularidadeExpandida(grafo):

	''' Essa irá calcular a qualidade da rede como um todo, após definida as comunidades '''

	pass


def calculaPesosIncidentes(grafo, verticesComunidade): ## tot


	''' Responsável por calcular o peso das arestas incidentes para cada um dos vértices '''
	if type(verticesComunidade) == int:
		vertice = verticesComunidade
		verticesComunidade = []
		verticesComunidade.append(vertice)	
	soma = 0
	for i in range(0, len(verticesComunidade)):
		vizinhos = grafo.neighborhood(vertices = verticesComunidade[i], mode = "IN")  ## pegando os vértices de entrada em cada um vértices da comunidade

		for j in range(0, len(vizinhos)):

			if vizinhos[j] != verticesComunidade[i]:
			
				idArestas = grafo.get_eids(pairs = [(vizinhos[j], verticesComunidade[i])], directed = True) ## pegando os ids das arestas entre aqueles vértices

				for k in idArestas:
					try:
						soma = grafo.e[k]['weight'] + soma
					except:
						soma = soma + 1

	return soma


def calculaPesoNo(grafo, vertice):

	vizinhos = grafo.neighborhood(vertices = vertice, mode = "ALL")
	soma = 0
	for j in vizinhos:

		if j != vertice:
			idArestas = grafo.get_eids(pairs = [(j, vertice)], directed = False)

			for k in idArestas:

				try:
					soma = grafo.e[k]['weight'] + soma
				except:
					soma = soma + 1

	return soma

def modularidadeLocal(grafo, comunidade):

	''' Método para cálculo da modularidade local, dos vértices que pertencem aquela comunidade
		A métrica utilizada neste trabalho foi retirada do trabalho de blondel (aquele em que ele
		define o algoritmo de multilevel) 
	 '''

	pesoTotal = calculaPesos(grafo)
	pesoComunidade = calculaPesos(comunidade)
	pesosIncidentesComunidade = calculaPesosIncidentes(grafo, comunidade.vs['id'])
	pesosIncidentesNo = calculaPesosIncidentes(grafo, comunidade.vs['id'][len(comunidade.vs['id'])-1])
	pesoNo = calculaPesoNo(grafo, comunidade.vs['id'][len(comunidade.vs['id'])-1])
	primeiraParte = ((pesoComunidade + pesoNo)/2*pesoTotal) - ((pesosIncidentesComunidade + pesosIncidentesNo)/(2*pesoTotal))**2
	segundaParte = (pesoComunidade/2*pesoTotal) - (pesosIncidentesComunidade/2*pesoTotal)**2 - (pesosIncidentesNo/2*pesoTotal)**2
	modularidade = primeiraParte - segundaParte

	return modularidade




