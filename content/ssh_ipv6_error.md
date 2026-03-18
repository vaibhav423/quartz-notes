in arch linux nmcli or network manager , set different ipv6 local link address per ssid
the fix is: 
do this for all ssid to keep a fixed address

nmcli connection edit Uniworld-1
set ipv6.addr-gen-mode eui64
save
q
