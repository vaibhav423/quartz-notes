---
tags:
  - Keep/Archived
---

# Block outbound DNS for clients
sudo iptables -t nat -I PREROUTING -i ap0 -p udp --dport 53 -j DNAT --to 192.168.177.119

# Force HTTP(S) to your own IP if needed
sudo iptables -t nat -I PREROUTING -i ap0 -p tcp --dport 80 -j DNAT --to-destination 192.168.177.119:80