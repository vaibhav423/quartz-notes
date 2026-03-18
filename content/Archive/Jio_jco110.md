### 📋 System Summary

| Category    | Value                            |
| ----------- | -------------------------------- |
| **CPU**     | 2× Broadcom BMIPS4350 @ ~400 MHz |
| **RAM**     | 491 MB total, 268 MB free        |
| **Swap**    | Not enabled                      |
| **Storage** | UBI filesystem, ~219 MB root     |
| **Kernel**  | 3.4.11-rt19 (MIPS)               |
| *Wifi*      | BCMxx (BCM43xx)                  |

---

### 🧠 Memory Info (`cat /proc/meminfo`)

- **Total RAM:** `491440 kB` (≈491 MB)  
- **Free RAM:** `268144 kB` (≈268 MB)  
- **Buffers:** `0 kB`  
- **Cached:** `40512 kB`  
- **Active:** `80224 kB`  
- **Inactive:** `21200 kB`  
- **SwapTotal:** `0 kB`  
- **SwapFree:** `0 kB`

---

### 💾 Storage (`df -h`)

| Filesystem         | Size   | Used  | Available | Use% | Mounted on |
|--------------------|--------|-------|-----------|------|------------|
| `ubi:rootfs_ubifs` | 219.1M | 53.2M | 165.9M    | 24%  | `/`        |
| `mtd:data`         | 4.0M   | 1.4M  | 2.6M      | 36%  | `/data`    |
| `mtd:bootfs`       | 3.9M   | 2.9M  | 1.0M      | 74%  | `/bootfs`  |

---

### 🔧 MTD Partitions (`cat /proc/partitions`)

```
major minor  #blocks  name
  31        0     255488 mtdblock0
  31        1     255488 mtdblock1
  31        2       4096 mtdblock2
  31        3        128 mtdblock3
  31        4     259456 mtdblock4
  31        5     259456 mtdblock5
  31        6       3968 mtdblock6
  31        7       3968 mtdblock7
  31        8     244652 mtdblock8
```

---

### ⚙️ CPU Info (`cat /proc/cpuinfo`)

- **System Type:** `968380F_JCO110`
- **Cores:** 2
- **Model:** Broadcom BMIPS4350 V8.0
- **Core 0 BogoMIPS:** 397.31  
- **Core 1 BogoMIPS:** 409.60  
- **TLB entries:** 32  
- **Shadow register sets:** 1  
- **Microsecond timers:** Yes  
- **Wait instruction:** Yes  

---

### 🖥️ Kernel Version (`uname -a`)

```
Linux reliance.reliance 3.4.11-rt19 #6 SMP PREEMPT Mon Dec 7 06:40:06 UTC 2020 mips GNU/Linux
``` 