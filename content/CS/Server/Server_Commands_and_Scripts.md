---
tags:
  - Keep/Archived
---

gzip -dk pass.json.gz

scp -r ec3:/home/ubuntu/p3 ~/

ssh ec3 "tail -f /home/ubuntu/log.txt"

server:


export START=1500001 END=1890000 SEM=10000
nohup python3 -u ultra.py >> log.txt 2>&1 &



echo strt - $START EnD - $END SEM - $SEM

mkdir -p trash && mv main.json.gz pass.json.gz second.json.gz trash/

mkdir -p p4 && mv main.json.gz pass.json.gz second.json.gz log.txt p4/