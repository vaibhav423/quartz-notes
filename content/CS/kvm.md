    <qemu:arg value="-device"/>
    <qemu:arg value="qemu-xhci,id=usb.0,bus=pcie.0,addr=0x4"/>
    <qemu:arg value="-videodev"/>
    <qemu:arg value="v4l2,device=/dev/video14,id=video0"/>
    <qemu:arg value="-device"/>
    <qemu:arg value="usb-video,videodev=video0"/>
