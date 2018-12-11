#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-
from igraph import *
import random
import bio_troy
import numpy as np
import matplotlib.pyplot as plt
import sys

def definePopulacao(vertices, numIndividuos, tamanhoIndividuo):

	''' Define os vértices que serão os individuos '''
	populacao = []
	for i in range(0, numIndividuos):
		if tamanhoIndividuo == 0:
			tamanhoIndividuo = random.randint(1, len(vertices)-1)
		else:
			if tamanhoIndividuo>len(vertices)-1:
				print("O tamanho do individuo não pode ser maior que o número de vértices !")
				exit()

		
		j=0
		individuo = []
		while(j<(tamanhoIndividuo)):
			gene = random.randint(0, len(vertices)-1)
			if not gene in individuo:
				individuo.append(gene)
				j=j+1

		populacao.append(individuo)

	return populacao


def selecaoTorneio(fit, melhoresComunidades):

	novaPopulacao = []
	for i in range(0, len(melhoresComunidades)):
		
		competidorUm = random.randint(0, len(melhoresComunidades)-1)
		competidorDois = random.randint(0, len(melhoresComunidades)-1)

		if fit[competidorDois] >= fit[competidorUm]:
			novaPopulacao.append(melhoresComunidades[competidorDois])
		else:
			novaPopulacao.append(melhoresComunidades[competidorUm])

	return novaPopulacao

def cruzamentoCorte(paiUm, paiDois):


	pInicial = int(len(paiUm)/3)
	meioUm = paiUm[pInicial:pInicial*2] ### coloquei metade um  meio do filho 1
	meioDois = paiDois[pInicial:pInicial*2]

	filhoUm = []
	filhoDois = []
	for i in meioUm: filhoUm.append(i)
	for i in meioDois: filhoDois.append(i)

	for i in paiDois:
		if not i in filhoUm:
			filhoUm.append(i)
	for i in paiUm:
		if not i in filhoDois:
			filhoDois.append(i)

	return filhoUm, filhoDois


def mutacao(taxaMutacao, individuo, grafo):


	x = random.uniform(0, 1)

	if x <= taxaMutacao:

		if len(individuo)>1:
			x = random.randint(1, len(individuo)-1)
			
			i=0
			while(i<x):
				
				vertice = random.randint(0, grafo.vcount()-1)
				if not vertice in individuo:
					individuo[random.randint(0, len(individuo)-1)] = vertice
					i=i+1


	return individuo

def grafica(x1):

	x = np.array(range(len(x1)))

	#plt.plot( x, x1, 'go') # green bolinha
	plt.plot( x, x1,color='red') # linha pontilha orange

	#plt.plot( x, x2, 'r^') # red triangul

	#plt.axis([-10, 60, 0, 11])
	plt.title("Algoritmo DCS")


	plt.grid(True)
	plt.xlabel("Gerações")
	plt.ylabel("Fitness")
	plt.show()


if __name__ == '__main__':
	
	random.seed()
	print("Número de seed -->", sys.argv[1] )
	print("Nome da Rede", sys.argv[2])
	quebraTexto = (sys.argv[2]).split('.')
	if quebraTexto[1] == "txt":
		grafo = Graph.Read_Ncol("REDE/"+sys.argv[2])
	else:
		grafo = Graph.Read_GML("REDE/"+sys.argv[2]) ### lendo o grafo no formato gml

	for i in range(0, grafo.vcount()): ## defino os ids 
		grafo.vs[i]['id'] = i

	populacao = definePopulacao(grafo.vs['id'], 100, int(sys.argv[1]))
	numGeracoes = 100
	melhorAtual = 0
	melhoresComunidades = []
	melhoresFitness = []
	taxaMutacao = 0.01
	for k in range(0, numGeracoes):

		fit = []
		for i in range(0, len(populacao)):
			fit.append(bio_troy.fitness(grafo, populacao[i]))
		
		if max(fit) > melhorAtual: ## atualizo o melhor elemento
			
			melhorAtual = max(fit)
			melhoresComunidades.append(populacao[fit.index(max(fit))])
		else: ### caso não seja melhor

			melhoresComunidades.append(populacao[fit.index(max(fit))])

		melhoresFitness.append(max(fit))

		## seleção

		fit, populacao = (list(x) for x in zip(*sorted(zip(fit, populacao), reverse=False)))
		selecionados = selecaoTorneio(fit, populacao)

		## cruzamento
		populacao = []
		for i in range(0, len(selecionados)-1, 2):
			filhoUm, filhoDois = cruzamentoCorte(selecionados[i], selecionados[i+1])
			populacao.append(filhoUm)
			populacao.append(filhoDois)
		
		populacao.pop(len(populacao)-1)
		populacao.append(melhoresComunidades[len(melhoresComunidades)-1])

		## mutação
		for i in range(0, len(populacao)):
			populacao[i] = mutacao(taxaMutacao, populacao[i], grafo)



	#print(max(melhoresFitness))
	bestSeeds = melhoresComunidades[melhoresFitness.index(max(melhoresFitness))]
	comunidades = []
	for i in bestSeeds:
		comunidades.append(bio_troy.expansaoDeVertices(i, grafo))

	#comunidades = set(comunidades)
	results = set(x for l in comunidades for x in l)


	'''print("------- Relatório-------")
	print("Vértices Iniciais ", bestSeeds)
	print("Comunidade Gerada ", comunidades)
	print("Indice de cobertura da Rede ", (len(list(results)))/grafo.vcount())
	print("Modularidade ", max(melhoresFitness))'''
	print(bestSeeds)
	try:
		arq = open("saida_"+quebraTexto[0]+".txt", 'a')
	except:
		arq = open("saida_"+quebraTexto[0]+".txt", 'w')

	### aqui estou imprimindo em arquivo para realizar testes
	### Estou imprimindo a quantidade de sementes, indice de cobertura, melhor fitness
	arq.write(str(len(bestSeeds))+'\t'+str((float(len(list(results))))/float(grafo.vcount()))+'\t'+str(max(melhoresFitness))+'\n')

	
	#grafica(melhoresFitness)
	
