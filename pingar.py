#!/usr/bin/python

import os
import threading

os.system("echo -n > /home/dtic/Documentos/trocar-ssid/ips-off.txt;echo -n > /home/dtic/Documentos/trocar-ssid/ips-on.txt")

def pingar(ip):
	os.system("/home/dtic/Documentos/trocar-ssid/ping.sh "+ip)
	
arquivo=open("/home/dtic/Documentos/trocar-ssid/ips","r")
ips=arquivo.readlines()

threads = []
for ip in ips:
	t = threading.Thread(target=pingar, args=[ip,])
	t.start()
	threads.append(t)

for av in threads:
	av.join()

#print "pingando"