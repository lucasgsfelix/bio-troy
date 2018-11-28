from igraph import *
import random
import modularidade
import copy

## BIO inspired algoriThm foR cOmmunitY detection with overlapping 

def defineVizinhos(grafo, vertice):

	try:
		vizinhos = grafo.neighborhood(vertices = vertice) ## retorna os vizinhos de um dado vértice
	except:
		vertice = modularidade.retornaIds(grafo, vertice)
		vizinhos = grafo.neighborhood(vertices = vertice)
	for i in range(0, len(vizinhos)): ### evitando self loops
		if vizinhos[i] == vertice:
			vizinhos.pop(i)
			break

	return vizinhos


def expansaoDeVertices(vertice, grafo):

	
	grafoComunidade = Graph(directed = grafo.is_directed()) ## criei uma nova estrutura de dados grafo
	grafoComunidade.add_vertices(1) ### adicionando um primeiro vértice

	grafoComunidade.vs[0]['id'] = vertice ## como id ele irá usar o id do grafo anterior

	modularidadeInicial = modularidade.modularidadeLocal(grafo, grafoComunidade) ### vou calcular modularidade para um vértice apenas
	visitados = []
	
	while(1): ## tenho que visitar a maior quantidade de vértices possíveis, até que não haja mais ganho de modularidade
		

		
		grafoBackup = copy.copy(grafoComunidade) ## estou fazendo uma cópia na memória, então eles não apontam para o mesmo lugar
		vizinhos = defineVizinhos(grafo, vertice) ### retorna os vizinhos de um vértice


		for i in range(0, len(vizinhos)):

			if not vizinhos[i] in visitados:
				
				grafoComunidade.add_vertices(1)
				grafoComunidade.vs[grafoComunidade.vcount()-1]['id'] = vizinhos[i] ## o último adicionado recebendo seu id

				verticesEscolhidos = []
				for v in grafoComunidade.vs(): ##tenho que pegar o objeto do vértice com aquele id
					if v['id'] == vizinhos[i]:
						verticesEscolhidos.append(v)
					elif v['id'] == vertice:
						verticesEscolhidos.append(v)

				

				try:
		
					grafoComunidade.add_edge(verticesEscolhidos[0], verticesEscolhidos[1], weight = grafo.es['weight'])
				except:
					grafoComunidade.add_edge(verticesEscolhidos[0], verticesEscolhidos[1], weight = 1)
				
				modularidadeNova = modularidade.modularidadeLocal(grafo, grafoComunidade)
	
				if modularidadeNova >= modularidadeInicial:
					modularidadeInicial = modularidadeNova
				else: ### quer dizer que a modularidade diminuiu
					grafoComunidade = grafoBackup ## então eu tenho que restaurar o grafo

				visitados.append(vertice)


		if vertice in visitados: ## todos já foram visitados
			break

		### agora eu tenho que ver o novo vértice
		for v in grafoComunidade.vs(): ## fazendo uma busca pelo próximo vértice
			if not v['id'] in visitados:
				vertice =  v['id'] ### definindo o novo vértice
				break

	return grafoComunidade.vs['id']


def fitness(grafo, populacao):
	

	comunidades = []
	for i in populacao: ### etapa de expansão para cada um dos vértices

		comunidades.append(expansaoDeVertices(i, grafo))
	
	modularidadeExtendida = modularidade.modularidadeExpandida(grafo, comunidades)
	
	return modularidadeExtendida
