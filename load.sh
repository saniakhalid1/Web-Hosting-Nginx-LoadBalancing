#!/bin/bash

for (( i=50; i<=20000; i+= 300))
do
	./httperf_script.sh $i 
done

