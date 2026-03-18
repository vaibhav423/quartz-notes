## cmd for port scan
sudo nmap -p- --open --min-rate 5000 -T4 -n --send-eth 192.168.1.1
## cmd to get venfor names with port 80
sudo nmap -p 80 --open --min-rate 5000 -T4 -n 192.168.0.0/19 | grep -E "Nmap scan report|MAC Address"
##
sudo nmap -p 34567 --open --min-rate 5000 -T4 -n 192.168.0.0/19
k
