#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-
import statistics
import sys
## código responsável por fazer média, desvio padrão de nossos valores
def leitura(arquivo):

	arq = open(arquivo, 'r')
	info = arq.read()
	arq.close()
	info = info.split('\n')

	nSeeds, iCobertura, fit = [], [], []
	for i in range(0, len(info)):
		info[i] = info[i].split('\t')
		if (info[i][0]=='' or info[i][0]==' '):
			break

		nSeeds.append(float(info[i][0]))
		iCobertura.append(float(info[i][1]))
		fit.append(float(info[i][2]))
	


	return nSeeds, iCobertura, fit

def estatisticas(info, flag, msg):

	estatisticas = []
	estatisticas.extend([statistics.mean(info), max(info), min(info), statistics.stdev(info)])

	'''print("Melhor ", min(info))
	print("Pior ", max(info))
	print("Média ", statistics.mean(info))
	print("Desvio padrão ", statistics.stdev(info))'''
	string = ''
	for i in range(0, len(estatisticas)):
		string =   string+ '&' +"$"+str(round(estatisticas[i], 2))+"$"

	if flag == 0:
		string = string + "\\\\ \\hline"
	else:
		string = string + "\\\\ \\cline{2-5}"

	string = msg + string + '\n'

	print(string)

	return string

quebraTexto = (sys.argv[1]).split('.')
nSeeds, iCobertura, fit = leitura("saida_"+quebraTexto[0]+'.txt')
#nSeeds, iCobertura, fit = leitura("saida_karate.txt")

try:
	arq = open("tabelaLatex_"+quebraTexto[0]+'.txt', 'a')
except:
	arq = open("tabelaLatex_"+quebraTexto[0]+'.txt', 'w')
arq.write(estatisticas(nSeeds, 1, "&Seeds")+estatisticas(iCobertura, 1, "&Cobertura") + estatisticas(fit, 0, "&Fitness"))


