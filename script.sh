numSeeds=2
#redes=("karate.gml" "jazz.txt" "metabolic.txt" "zebra.txt" "dolphins.txt")
redes=("dolphins.txt" "zebra.txt")
for rede in $redes; do
	while [ $numSeeds -lt 6 ]; do
		contador=0
		echo "Este é o numero de seed ", $numSeeds 
		echo $rede
		while [ $contador -lt 10 ]; do 
			python algoritmoGenetico.py $numSeeds $rede
			let contador=contador+1;
		done
		echo "Agora está sendo realizada as estatísticas para ", $numSeeds
		python estatisticas.py $rede
		$rede | cut -d'.' -f1 | rm "saida_$rede.txt"
		let numSeeds=numSeeds+1;

	done

done
