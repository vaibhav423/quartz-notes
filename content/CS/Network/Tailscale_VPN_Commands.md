---
tags:
  - Keep/Archived
---

am broadcast -a com.tailscale.ipn.CONNECT_VPN -n com.tailscale.ipn/.IPNReceiver


am broadcast -a com.tailscale.ipn.DISCONNECT_VPN -n com.tailscale.ipn/.IPNReceiver


am broadcast -a com.tailscale.ipn.ENABLE_EXIT_NODE -n com.tailscale.ipn/.IPNReceiver

am broadcast -a com.tailscale.ipn.DISABLE_EXIT_NODE -n com.tailscale.ipn/.IPNReceiver