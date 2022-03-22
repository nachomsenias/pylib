#!/bin/bash

# indices tp0 tp12 tp25 para los cuatro algos
# valores de r=25, r=50, r=100, r=200

path="/home/ignacio/proyectos/MM-MO/Data/soluciones/mograms/"

for index in 0 12 25
do
	echo "#####Running problem TP${index}#####"

	for algo in NSGAIIOriginal0 Omni0 Omni0.1 Omni0.05;
	do
		echo "###Method: ${algo}###"
		for file in "${path}${algo}/TP${index}/Pajek"*"tsv_mograms"; 
		do 
			echo "Current file: ${file}";
			python DrawPajek.py "$file"; 
		done
	done
done
