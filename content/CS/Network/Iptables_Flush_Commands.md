---
tags:
  - Keep/Archived
---

sudo iptables -F
sudo iptables -X
sudo iptables -t nat -F
sudo iptables -t nat -X
su -c "echo 1 > /proc/sys/net/ipv4/ip_forward"