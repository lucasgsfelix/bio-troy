from igraph import *
import random
import modularidade



def definePopulacao(vertices, numIndividuos):

	''' Define os vértices que serão os individuos '''
	populacao = []
	for i in range(0, numIndividuos):
		populacao.append(random.randint(0, len(vertices)))

	return populacao




def expansaoDeVertices(vertice, grafo):

	vizinhos = grafo.neighborhood(vertices = vertice) ## retorna os vizinhos de um dado vértice
	grafoComunidade = Graph() ## criei uma nova estrutura de dados grafo
	grafoComunidade.add_vertices(1) ### adicionando um primeiro vértice
	grafoComunidade.vs[0]['id'] = vertice ## como id ele irá usar o id do grafo anterior
	modularidadeInicial = modularidade.modularidadeLocal(grafo, grafoComunidade) ### vou calcular modularidade para um vértice apenas
	print(modularidadeInicial)
	for i in range(0, len(vizinhos)):
		pass




if __name__ == '__main__':
	
	random.seed()
	grafo = Graph.Read_GML("REDE/karate.gml") ### lendo o grafo no formato gml
	populacao = definePopulacao(grafo.vs['id'], 3)
	numGeracoes = 100


	for k in range(0, numGeracoes):

		for i in populacao: ### etapa de expansão para cada um dos vértices

			expansaoDeVertices(i, grafo)
			exit()





