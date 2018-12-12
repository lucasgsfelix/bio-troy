import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import matplotlib.mlab as mlab
def imprimeGrafico(x, yZachary, yDolphins, yZebras):

	plt.plot(x, yZachary, color = 'green', label = 'Zachary') #'go', color='orange',  label = 'Reais', alpha = 0.5, linewidth = 5, markersize = 6)  # linha tracejada azul
	plt.plot(x, yDolphins, color = 'orange', label = 'Dolphins')
	plt.plot(x, yZebras, color = 'blue', label = 'Zebras')

	plt.legend(loc = 'upper right')
	plt.title("Variação do Nº de Comunidades")
	plt.grid(True) ### imprimindo as grades atrás
	plt.xlabel("Quant. Seeds")
	plt.ylabel("Nº Comunidades")
	plt.show()


def graficoPizza():

	labels = 'Python', 'C++', 'Ruby', 'Java'
	sizes = [215, 130, 245, 210]
	colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
	explode = (0.1, 0, 0, 0)  # explode 1st slice
	 
	# Plot
	plt.pie(sizes, explçode=explode, labels=labels, colors=colors,
	        autopct='%1.1f%%', shadow=True, startangle=140)
	 
	plt.axis('equal')
	plt.show()

def fazHistograma():
	y = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2, 2, 6]

	mu, sigma = 10000, 1500
	#x = mu + sigma*np.random.randn(10000)

	# the histogram of the data
	n, bins, patches = plt.hist(y, normed = False, bins = 10, facecolor='blue')

	# add a 'best fit' line
	(mu, sigma) = norm.fit(y)
	y = mlab.normpdf( bins, mu, sigma)
	l = plt.plot(bins, y, 'r--', linewidth=2)

	plt.xlabel('Publicações')
	plt.ylabel('Quant. de Publições do Autor')
	plt.title('Quantidade de publicações por autor')

	plt.grid(True)

	plt.show()

def leitura(arquivo):

	arq = open(arquivo,'r')
	info = arq.read()
	info = info.split('\n')

	x = [2,3,4,5]
	yZachary, yDolphins, yZebras = [], [], []
	for i in range(0, len(info)):
		info[i] = info[i].split('\t')
		yZachary.append(float(info[i][1]))
		yDolphins.append(float(info[i][2]))
		yZebras.append(float(info[i][3]))

	return x, yZachary, yDolphins, yZebras
	


x, yZachary, yDolphins, yZebras = leitura('numComunidades')
imprimeGrafico(x, yZachary, yDolphins, yZebras)