---
tags:
  - Keep/Archived
---

on server

sudo ip route add 192.168.0.0/16 via 10.7.0.2 dev wg0
sudo iptables -t nat -A POSTROUTING -s 10.7.0.0/24 -d 192.168.0.0/16 -j MASQUERADE

on client 

sudo iptables -t nat -A POSTROUTING -s 10.7.0.1/32 -d 192.168.0.0/16  -j MASQUERADE
su -c "echo 1 > /proc/sys/net/ipv4/ip_forward"
sudo iptables -A FORWARD -i tun0 -o wlan0 -j ACCEPT
sudo iptables -A FORWARD -i wlan0 -o tun0 -j ACCEPT
sudo iptables -A INPUT -p icmp -j ACCEPT
sudo iptables -A OUTPUT -p icmp -j ACCEP