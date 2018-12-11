contador=0
while [ $contador -lt 10 ]; do 
	python algoritmoGenetico.py 0 "zebra.txt"
	let contador=contador+1;
done