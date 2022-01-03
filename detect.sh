#!/bin/bash

#ipv4_addr=(198.41.0.4 199.9.14.201 192.33.4.12 199.7.91.13 192.203.230.10 192.5.5.241 192.112.36.4 198.97.190.53 192.36.148.17 192.58.128.30 193.0.14.129 199.7.83.42 202.12.27.33)
ip_addr=(a.root-servers.net b.root-servers.net c.root-servers.net d.root-servers.net e.root-servers.net f.root-servers.net g.root-servers.net h.root-servers.net i.root-servers.net j.root-servers.net k.root-servers.net l.root-servers.net m.root-servers.net)
REF_ipv4=(223.5.5.5 114.114.114.114 119.29.29.29)
REF_ipv6=(2400:3200::1 2409:8088::a 2402:4e00::)

raw_data_detect(){
	
	for RSI in ${ip_addr[@]}
	do
	{
	 file="./raw_data/raw_data_"${RSI:0:1}".txt"
	 exec 1> $file
	 date +%Y-%m-%dT%H:%M:%SZ
	 echo $RSI
		
		dig @$RSI +noedns +short CHAOS TXT hostname.bind
		
		dig @$RSI +notcp -4 IN NS
		dig @$RSI +tcp -4 IN NS
		#dig @$RSI +notcp -6 IN NS
		#dig @$RSI +tcp -6 IN NS
		
		#traceroute -n $RSI -4 53
		#traceroute -n $RSI -6 53
		traceroute $RSI -I 53
		
		for REF in ${REF_ipv4[@]}
		do
			dig @$REF +noedns IN NS
		done
		for REF in ${REF_ipv6[@]}
		do
			dig @$REF +noedns IN NS
		done
		
		dig @$RSI errcom +nord
		
		for ns in $(dig +short akamai.net NS) 
		do 
			dig -4 +short @$ns whoami.akamai.net A
			#dig -6 +short @$ns whoami.akamai.net AAAA
		done
	 
	}&
	done
	wait
}

raw_data_handle(){
	python raw_data_handle.py
}

raw_data_detect

raw_data_handle




