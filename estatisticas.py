import statistics
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

def estatisticas(info, flag):

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

	string = string + '\n'

	return string


nSeeds, iCobertura, fit = leitura("saida.txt")
arq = open("tabelaLatex.txt", 'a')
arq.write(estatisticas(info, 1)+estatisticas(iCobertura, 1) + estatisticas(fit, 0))


