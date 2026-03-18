---
tags:
  - Keep/Archived
---

socat -d -d UDP-LISTEN:51839,fork TCP:127.0.0.1:51839

socat -d -d TCP-LISTEN:51822,fork UDP:127.0.0.1:51822