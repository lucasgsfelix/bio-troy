from igraph import *
import random
import bio_troy

def definePopulacao(vertices, numIndividuos):

	''' Define os vértices que serão os individuos '''
	populacao = []
	for i in range(0, numIndividuos):
		tamanhoIndividuo = random.randint(1, len(vertices)-1)
		j=0
		individuo = []
		while(j<(tamanhoIndividuo)):
			gene = random.randint(0, len(vertices))
			if not gene in individuo:
				individuo.append(gene)
				j=j+1

		populacao.append(individuo)

	return populacao


if __name__ == '__main__':
	
	random.seed()
	grafo = Graph.Read_GML("REDE/karate.gml") ### lendo o grafo no formato gml
	populacao = definePopulacao(grafo.vs['id'], 100)
	numGeracoes = 100
	teste = []
	for i in range(0, len(populacao)):
		teste.append(bio_troy.fitness(grafo, populacao[i]))
	print(max(teste))