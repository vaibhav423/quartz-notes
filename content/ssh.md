# The Complete SSH & SSHD File System Reference

This document provides a deep dive into every standard file and directory used by the OpenSSH client (`ssh`) and server (`sshd`).

---

## 1. Client-Side (User) Configuration: `~/.ssh/`
This directory is located in the user's home folder and contains personal keys and configuration.

| File/Directory | Description |
| :--- | :--- |
| `~/.ssh/` | The base directory for user SSH files. **Permissions: 700** |
| `~/.ssh/id_ed25519` | Your **Private Key**. This is your digital identity. **Never share this.** |
| `~/.ssh/id_ed25519.pub`| Your **Public Key**. This is the "lock" you place on servers. |
|                         | (i.e inside `~/.ssh/authorized_keys` on the servers) using command for example |
|                         | `ssh-copy-id -p 8022 ixdire@fe80::3e56:2959:f13a:a1a9%wlan0`                     |
| `~/.ssh/authorized_keys`| The "Guest List." Contains public keys allowed to log into this account. |
| `~/.ssh/known_hosts` | A database of "Host Keys" for servers you have previously visited. |
| `~/.ssh/config` | User-specific aliases and settings (e.g., nicknames for IPs). |
| `~/.ssh/rc` | Commands in this file are executed by SSH when the user logs in. |

---

## 2. Server-Side (Global) Configuration: `/etc/ssh/`
These files define how the SSH Daemon (`sshd`) behaves for the entire system.

| File/Directory | Description |
| :--- | :--- |
| `/etc/ssh/sshd_config` | The primary server configuration file (Ports, Auth methods, etc.). |
| `/etc/ssh/sshd_config.d/`| Directory for modular server config snippets (`*.conf`). |
| `/etc/ssh/ssh_config` | The default configuration for the SSH **client** for all users. |
| `/etc/ssh/ssh_config.d/` | Directory for modular client config snippets (`*.conf`). |
| `/etc/ssh/ssh_host_*_key`| The server's **Private Host Keys**. Proves server identity to clients. |
| `/etc/ssh/ssh_host_*.pub`| The server's **Public Host Keys**. Shared with clients upon connection. |
| `/etc/ssh/moduli` | Contains Diffie-Hellman groups used for secure key exchange. |

---

## 3. System Binaries & Helper Tools
Where the actual "engines" of SSH live.

| Path | Purpose |
| :--- | :--- |
| `/usr/bin/ssh` | The client binary used to connect to other machines. |
| `/usr/sbin/sshd` | The server daemon binary that listens for connections. |
| `/usr/bin/ssh-keygen` | The tool used to create new public/private key pairs. |
| `/usr/bin/ssh-agent` | A background program that holds decrypted keys in memory. |
| `/usr/bin/scp` | Secure Copy: Uses SSH to move files between machines. |
| `/usr/libexec/sftp-server`| The backend engine that handles SFTP file transfers. |

---

## 4. Operational & Log Files
Where the system tracks active sessions and security events.

| Path | Purpose |
| :--- | :--- |
| `/var/log/auth.log` | **Security Log:** Records every login attempt (Ubuntu/Debian). |
| `/var/log/secure` | **Security Log:** Records every login attempt (RHEL/CentOS/Fedora). |
| `/run/sshd.pid` | Contains the Process ID of the currently running SSH daemon. |
| `/tmp/ssh-XXXXX/` | Temporary sockets created when using **SSH Agent Forwarding**. |

---

## 5. Summary of Key Permissions
SSH will often fail silently or throw errors if these permissions are not exactly right.

| Target | Recommended Permission | Command |
| :--- | :--- | :--- |
| User `.ssh` folder | `drwx------` (700) | `chmod 700 ~/.ssh` |
| Private Keys | `-rw-------` (600) | `chmod 600 ~/.ssh/id_ed25519` |
| Public Keys | `-rw-r--r--` (644) | `chmod 644 ~/.ssh/*.pub` |
| `authorized_keys` | `-rw-------` (600) | `chmod 600 ~/.ssh/authorized_keys` |
| `config` file | `-rw-------` (600) | `chmod 600 ~/.ssh/config` |
| Host Keys (Private) | `-rw-------` (600) | Only root should have access. |
