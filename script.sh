numSeeds=0
redes=("karate.gml" "jazz.txt" "metabolic.txt")
#redes=("jazz.txt" "metabolic.txt")
for rede in $redes; do
	while [ $numSeeds -lt 6 ]; do
		contador=4
		echo "Este é o numero de seed ", $numSeeds 
		echo $rede
		while [ $contador -lt 10 ]; do 
			python algoritmoGenetico.py $numSeeds $rede
			let contador=contador+1;
		done
		echo "Agora está sendo realizada as estatísticas para ", $numSeeds
		python estatisticas.py $rede
		rm saida.txt
		>> saida.txt
		let numSeeds=numSeeds+1;
		break;
	done
	break;
done
