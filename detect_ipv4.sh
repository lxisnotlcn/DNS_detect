#!/bin/bash

REF_ipv4=(223.5.5.5 114.114.114.114 119.29.29.29)

i=0
for var in "$@"
do
	env[$i]=$var
	i=`expr $i + 1`
done

for((j=0;j<$i-2;j++))
do
	ip_addr[$j]=${env[$j+2]}
done

for RSI in ${ip_addr[@]}
do
{
	file="./raw_data/ipv4/raw_data_"${RSI:0:1}".txt"
	exec 1> $file
	echo "******"
	for ns in $(dig +short akamai.net NS) 
	do 
		dig -4 +short @$ns whoami.akamai.net A
	done
	echo "******"
	dig @$RSI +notcp -4 IN NS
	echo "******"
	dig @$RSI +tcp -4 IN NS
	
	if [ "${env[0]}" = "-t" ]
	then
		echo "******"
		traceroute $RSI -I 53
	fi
	
	if [ "${env[1]}" = "-r" ]
	then
		for REF in ${REF_ipv4[@]}
		do
			echo "******"
			dig @$REF +noedns IN NS
		done
	fi
	
}&
done
wait






