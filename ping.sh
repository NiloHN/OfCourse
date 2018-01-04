#!/bin/sh

host=$1
ping -c1 -w1 $host > /dev/null 2>&1
if [ $? -eq 0 ]
then
	echo  "$1" >> /home/dtic/Documentos/trocar-ssid/ips-on.txt
	exit 0
else
	echo  "$1" >> /home/dtic/Documentos/trocar-ssid/ips-off.txt
	exit 1
fi
