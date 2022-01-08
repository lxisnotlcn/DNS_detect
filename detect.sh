#!/bin/bash

for RSI in "$@"
do
{
	file="./raw_data/raw_data_"${RSI:0:1}".txt"
	exec 1> $file
	echo "******"
	date +%Y-%m-%dT%H:%M:%SZ
	echo "******"
	dig @$RSI +noedns +short CHAOS TXT hostname.bind
	echo "******"
	dig @$RSI errcom +nord
	
	
}&
done
wait

