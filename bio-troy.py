from igraph import *
import random
import modularidade


## BIO inspired algoriThm foR cOmmunitY detection with overlapping 
def definePopulacao(vertices, numIndividuos):

	''' Define os vértices que serão os individuos '''
	populacao = []
	for i in range(0, numIndividuos):
		populacao.append(random.randint(0, len(vertices)))

	return populacao




def expansaoDeVertices(vertice, grafo):

	vizinhos = grafo.neighborhood(vertices = vertice) ## retorna os vizinhos de um dado vértice

	grafoComunidade = Graph(directed = grafo.is_directed()) ## criei uma nova estrutura de dados grafo
	grafoComunidade.add_vertices(1) ### adicionando um primeiro vértice
	grafoComunidade.vs[0]['id'] = vertice ## como id ele irá usar o id do grafo anterior
	modularidadeInicial = modularidade.modularidadeLocal(grafo, grafoComunidade) ### vou calcular modularidade para um vértice apenas
	
	for i in range(0, len(vizinhos)): ### evitando self loops
		if vizinhos[i] == vertice:
			vizinhos.pop(i)
			break
	
	for i in range(0, len(vizinhos)):
		grafoComunidade.add_vertices(1)
		grafoComunidade.vs[grafoComunidade.vcount()-1]['id'] = vizinhos[i] ## o último adicionado recebendo seu id


		#idArestas = grafo.get_eids(pairs = [(vizinhos[i], vertice)], directed = False)
		#for j in idArestas:

		try:
			grafoComunidade.add_edge(vertice, grafoComunidade.vs[grafoComunidade.vcount()-1]['id'], weight = grafo.es['weight'])
		except:
			print(vertice, grafoComunidade.vs[len(grafoComunidade.vs)-1]['id'])
			print(grafoComunidade.vs['id'])
			print(vizinhos[i])
			grafoComunidade.add_edge(vertice, vizinhos[i], weight = 1)
		
		modularidadeNova = modularidade.modularidadeLocal(grafo, grafoComunidade)

		print(modularidadeNova, modularidadeInicial)
		exit()







if __name__ == '__main__':
	
	random.seed()
	grafo = Graph.Read_GML("REDE/karate.gml") ### lendo o grafo no formato gml
	populacao = definePopulacao(grafo.vs['id'], 3)
	numGeracoes = 100


	for k in range(0, numGeracoes):

		for i in populacao: ### etapa de expansão para cada um dos vértices

			expansaoDeVertices(i, grafo)
			exit()





