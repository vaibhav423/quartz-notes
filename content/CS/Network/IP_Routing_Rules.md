---
tags:
  - Keep/Archived
---

ip rule add table 5000 priority 5000
ip route add 10.5.0.0/24 dev tun0 table 5000
ip route add default dev ccmni0 table 5000






echo -n 1 >/proc/sys/net/ipv4/ip_forward
iptables -I FORWARD -i tun+ -j ACCEPT
iptables -I FORWARD -o tun+ -j ACCEPT
iptables -t nat -I POSTROUTING -o ccmni0 -j MASQUERADE
