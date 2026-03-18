---
tags:
  - Keep/Archived
---


#only for http traffic captive portal

iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
iptables -F
iptables -t nat -F



#This for showing web page on visit in any Web page on client device

dnsmasq --conf-file=/data/data/com.termux/files/usr/etc/dnsmasq.conf --pid-file=/data/data/com.termux/files/usr/var/run/dnsmasq.pid


iptables -t nat -A PREROUTING -p tcp --dport 443 -j REDIRECT --to-port 8080

iptables -t nat -A PREROUTING -p udp --dport 53 -j REDIRECT --to-port 53


iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080 


ps -ef | grep dnsmasq


nano /data/data/com.termux/files/usr/etc/dnsmasq.conf
