#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-
def calculaPesos(grafo):

	'''Responsável por calcular o peso das arestas quando há e quando não há pesos'''


	try:
		pesoTotal = sum(grafo.es['weight'])
	except:
		pesoTotal = grafo.ecount()


	return pesoTotal

def contaComunidades(vertice, comunidades):

	quantComunidades = 0
	for i in comunidades:
		if vertice in i :
			quantComunidades = quantComunidades + 1


	return quantComunidades


def modularidadeExpandida(grafo, comunidades): 

	A = grafo.get_adjacency()
	''' Essa irá calcular a qualidade da rede como um todo, após definida as comunidades '''
	m=1.0/(2*grafo.ecount())
	soma = 0
	for v in grafo.vs():
		for w  in grafo.vs():
			for k in comunidades:
				if (v.index in k) and (w.index in k):
					ov = contaComunidades(v.index, comunidades)
					ow = contaComunidades(w.index, comunidades)
					
					#primeiraParte = (1.0/(ov*ow))
					primeiraParte = 1

					kv = grafo.degree(vertices = v, mode = "ALL")
					kw = grafo.degree(vertices = w, mode = "ALL")

					segundaParte = (A[v.index][w.index]-(kv*kw*m))


					
					soma = (primeiraParte*segundaParte) + soma

	soma = m*soma

	
	return soma

def retornaIds(grafo, lista):

	if type(lista)==int or type(lista)==float:
		for v in grafo.vs():
			if int(lista) == int(v['id']):
				return v
	ids = []
	for i in lista:
		for v in grafo.vs():
			if i == v['id']:
				ids.append(v)

	return ids


def calculaPesosIncidentes(grafo, verticesComunidade): ## tot


	''' Responsável por calcular o peso das arestas incidentes para cada um dos vértices '''
	if type(verticesComunidade) == int:
		vertice = verticesComunidade
		verticesComunidade = []
		verticesComunidade.append(vertice)	
	soma = 0
	#verticesComunidade = retornaIds(grafo, verticesComunidade)
	for i in range(0, len(verticesComunidade)):
		
		try:
			vizinhos = grafo.neighborhood(vertices = verticesComunidade[i], mode = "IN")  ## pegando os vértices de entrada em cada um vértices da comunidade
		except:
			lista = []
			lista.append(verticesComunidade[i])
			lista = retornaIds(grafo, lista)
			vizinhos = grafo.neighborhood(vertices = lista[0], mode = "IN")
		#vizinhos = retornaIds(grafo, vizinhos)
		for j in range(0, len(vizinhos)):

			if vizinhos[j] != verticesComunidade[i]:
				

				try:
					idArestas = grafo.get_eids(pairs = [(vizinhos[j], verticesComunidade[i])], directed = True) ## pegando os ids das arestas entre aqueles vértices
				except:
					vizinhos[j] = retornaIds(grafo, vizinhos[j])
					verticesComunidade[i] = retornaIds(grafo, verticesComunidade[i])
					try:
						idArestas = grafo.get_eids(pairs = [(vizinhos[j], verticesComunidade[i])], directed = True)
					except:
						idArestas = []

				for k in idArestas:
					try:
						soma = grafo.e[k]['weight'] + soma
					except:
						soma = soma + 1

	return soma


def calculaPesoNo(grafo, vertice):

	try:
		vizinhos = grafo.neighborhood(vertices = vertice, mode = "ALL")
	except:
		vertice = retornaIds(grafo, vertice)
		vizinhos = grafo.neighborhood(vertices = vertice, mode = "ALL")
	soma = 0
	vizinhos = retornaIds(grafo, vizinhos)
	for j in vizinhos:

		if j != vertice:
			try:
				idArestas = grafo.get_eids(pairs = [(j, lista[0])], directed = False)
			except:
				idArestas = []
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


	indiceModularidade = 0
	pesoTotal = calculaPesos(grafo)
	pesoComunidade = calculaPesos(comunidade)
	pesosIncidentesComunidade = calculaPesosIncidentes(grafo, comunidade.vs['id'])
	pesosIncidentesNo = calculaPesosIncidentes(grafo, comunidade.vs['id'][len(comunidade.vs['id'])-1])
	pesoNo = calculaPesoNo(grafo, comunidade.vs['id'][len(comunidade.vs['id'])-1])


	primeiraParte = ((pesoComunidade + pesoNo)/(2.0*pesoTotal)) - ((pesosIncidentesComunidade + pesosIncidentesNo)/(2.0*pesoTotal))**2
	segundaParte = (pesoComunidade/(2.0*pesoTotal)) - (pesosIncidentesComunidade/(2.0*pesoTotal))**2 - (pesosIncidentesNo/(2.0*pesoTotal))**2
	indiceModularidade = primeiraParte - segundaParte
	
	return indiceModularidade




