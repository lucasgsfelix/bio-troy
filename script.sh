numSeeds=2
while [ $numSeeds -lt 6 ]; do
	contador=0
	echo "Este é o numero de seed ", $numSeeds
	while [ $contador -lt 10 ]; do 
		python algoritmoGenetico.py $numSeeds
		let contador=contador+1;
	done
	echo "Agora está sendo realizada as estatísticas para ", $numSeeds
	python estatisticas.py
	rm saida.txt
	>> saida.txt
	let numSeeds=numSeeds+1;
done
