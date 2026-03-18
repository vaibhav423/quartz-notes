---
tags:
  - Keep/Archived
---

in captive portal unable to block ipv6 traffic , hostpot-user are able to ping6 , ipv4 blockable

in setting up wifi and mobile data together ipv6 not working , ipv4 working 

ip -6 route get 2001:4860:4860::8888 2>/dev/null | grep -oP 'dev \K\S+'
sudo ip -6 route add default dev ccmni1 table 200
sudo ip -6 rule add from all lookup 200 pref 1600 