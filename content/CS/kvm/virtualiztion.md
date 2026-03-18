# virtualization
## EDK2 OVMF Summary

* **EDK2 (EFI Development Kit II):** An open-source, industrial-grade implementation of the **UEFI** (Unified Extensible Firmware Interface) specification.
* **OVMF (Open Virtual Machine Firmware):** A specific build of EDK2 designed to enable **UEFI support** for virtual machines.

### Core Function
It acts as the **virtual UEFI firmware** for QEMU/KVM, replacing the legacy **SeaBIOS**.

### Key Advantages
* **Modern Booting:** Enables support for **GPT** partitions and disks larger than 2TB.
* **Security:** Provides the framework for **Secure Boot** and virtual TPM (vTPM) integration.
* **Hardware Passthrough:** Critical for **GPU Passthrough** (VFIO) to allow guest OS drivers to initialize physical hardware correctly.
* **OS Compatibility:** Required for Windows 11 and modern Linux distributions that mandate UEFI.

### Implementation
Typically consists of two parts:
1.  **`OVMF_CODE.fd`**: The read-only firmware executable.
2.  **`OVMF_VARS.fd`**: The persistent "NVRAM" that stores UEFI settings and boot variables.
