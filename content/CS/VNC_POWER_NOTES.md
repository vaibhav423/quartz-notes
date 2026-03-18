VNC + XFCE Desktop and Temporary Power-Saving Notes

This note documents how to start the X (VNC) desktop, apply the temporary
power-saving steps we used, how processes were killed, and other important
notes (revert steps, safety warnings). Keep this file for later reference.

Environment specifics (current):
- VNC display: :2
- VNC port: 5902 (Xvnc listening on all interfaces)
- Xvnc log: /tmp/xvnc-2.log
- XFCE startup log: /home/ixdire/vnc-xfce.log
- User: ixdire

1) Start the X (VNC) desktop

- Start Xvnc on display :2 (listens on all interfaces):
  nohup Xvnc :2 -geometry 1280x800 -SecurityTypes None > /tmp/xvnc-2.log 2>&1 &

- Start XFCE on that display as the user (clean DBus session):
  # run as user ixdire (example shown with su)
  su -l ixdire -c "DISPLAY=:2 dbus-run-session -- startxfce4 > /home/ixdire/vnc-xfce.log 2>&1 &"

- Connect with a VNC client to host:5902 (or tunnel: ssh -L 5902:localhost:5902 user@host).

2) Useful checks and logs

- Check services and listening ports:
  ss -tnlp | grep -E '(:22|:5902)'
- Show the Xvnc and XFCE processes:
  ps -u ixdire | egrep 'Xvnc|xfce|dbus'
- Tail logs:
  tail -f /tmp/xvnc-2.log /home/ixdire/vnc-xfce.log

3) Temporary power-saving steps (what was applied)

- Stop/quiet user GUI services (temporary):
  su -l ixdire -c 'systemctl --user stop start-hyprland || true'
  su -l ixdire -c 'systemctl --user stop pipewire wireplumber || true'

- Kill heavy GUI apps (graceful then force):
  pkill -15 -u ixdire -f firefox
  pkill -15 -u ixdire -f kitty
  sleep 2
  pkill -9 -u ixdire -f firefox   # only if still present

- Set CPU governor to powersave (temporary):
  for c in /sys/devices/system/cpu/cpu[0-9]*; do
    govfile="$c/cpufreq/scaling_governor"
    [ -f "$govfile" ] && echo powersave | sudo tee "$govfile"
  done

- Run powertop auto-tune (if available):
  sudo powertop --auto-tune   # temporary until reboot

- Reduce display backlight (temporary):
  # set to ~15% of max
  for d in /sys/class/backlight/*; do
    max=$(cat "$d/max_brightness")
    new=$(( (max*15 + 99)/100 ))
    [ $new -lt 1 ] && new=1
    echo $new | sudo tee "$d/brightness"
  done

- Block Bluetooth (temporary):
  sudo rfkill block bluetooth

- NVIDIA: reduce power limit (temporary)
  # Only if nvidia-smi is available. Query limits first.
  nvidia-smi --query-gpu=power.min_limit,power.max_limit --format=csv,noheader,nounits
  sudo nvidia-smi -pm 1
  sudo nvidia-smi -pl <target-Watts>

4) What was killed / stopped

- The cleanup targeted user GUI/background processes so only SSH and VNC
  remained. Examples of targets (may differ on your system): firefox, kitty,
  aria2c, blueman, pipewire/wireplumber, nm-applet, hyprland, waybar, rclone
  (if you requested stopping mounts).

- The steps used: pkill -15 (graceful) then pkill -9 (force) for remaining PIDs.

5) How to revert (undo temporary changes)

- Restart stopped user services (as ixdire):
  systemctl --user start pipewire wireplumber
  systemctl --user start start-hyprland   # if you want to resume Hyprland

- Restore CPU governor to performance:
  for c in /sys/devices/system/cpu/cpu[0-9]*; do
    govfile="$c/cpufreq/scaling_governor"
    [ -f "$govfile" ] && echo performance | sudo tee "$govfile"
  done

- Unblock Bluetooth:
  sudo rfkill unblock bluetooth

- Restore backlight (example set to max):
  for d in /sys/class/backlight/*; do
    max=$(cat "$d/max_brightness")
    echo $max | sudo tee "$d/brightness"
  done

- Reset NVIDIA power limit (if changed):
  sudo nvidia-smi -pl <max-from-query>   # or sudo nvidia-smi -pm 0

- Re-launch killed apps manually (or reboot to fully restore session state).

6) Safety notes and caveats

- I preserved system sshd (PID 732 on this machine) so your remote connection
  should not be interrupted. Because your SSH session uses wlan0, I did NOT
  toggle Wi‑Fi; do not disable the interface holding your SSH session.
- Do NOT turn the fan off. Stopping fans risks hardware damage. Instead reduce
  heat (lower CPU freq/TDP, stop heavy processes) and let the fan idle.
- Offlining CPU cores or unloading GPU drivers saves power but may kill
  important processes or break the desktop; avoid unless you accept the risk.
- Many user services are managed by systemd user units and may respawn unless
  you disable the unit (systemctl --user disable <unit>). Killing a process
  without disabling its unit may cause it to restart.

7) Persistent options (if you later want them)

- Install TLP for persistent power profile: (Arch example)
  sudo pacman -S tlp
  sudo systemctl enable --now tlp

- Create a systemd user unit to start VNC + XFCE for automatic remote desktop
  on login/boot. Example unit: ~/.config/systemd/user/vnc-xfce.service

8) Handy commands summary (copy/paste)

- Start VNC+XFCE:
  nohup Xvnc :2 -geometry 1280x800 -SecurityTypes None > /tmp/xvnc-2.log 2>&1 &
  su -l ixdire -c "DISPLAY=:2 dbus-run-session -- startxfce4 > /home/ixdire/vnc-xfce.log 2>&1 &"

- Apply power-saves (temporary):
  for c in /sys/devices/system/cpu/cpu[0-9]*; do govfile="$c/cpufreq/scaling_governor"; [ -f "$govfile" ] && echo powersave | sudo tee "$govfile"; done
  sudo powertop --auto-tune
  sudo rfkill block bluetooth

- Kill heavy apps example:
  pkill -15 -u ixdire -f firefox || true; sleep 2; pkill -9 -u ixdire -f firefox || true

- Revert: start services, restore governor and backlight (see section 5 above).

9) Where to look for help / logs

- Xvnc log: /tmp/xvnc-2.log
- XFCE log: /home/ixdire/vnc-xfce.log
- Systemd journal (system): sudo journalctl -b -u sshd
- User journal (user services): journalctl --user -b

If you want, I can:
- create a systemd user unit to start/stop the VNC desktop safely;
- prepare a small script that applies these temporary power-savings and a
  companion script to revert them; or
- disable the specific systemd user units permanently (if you later decide).

--- End of note
