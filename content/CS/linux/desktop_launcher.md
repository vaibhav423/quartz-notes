# main
the core path which is looked by app launchers $XDG_DATA_DIRS
# command to search any desktop launcher
for dir in $(echo $XDG_DATA_DIRS | tr ':' ' '); do
    find "$dir" -name "*digikam*.desktop" 2>/dev/null
done

