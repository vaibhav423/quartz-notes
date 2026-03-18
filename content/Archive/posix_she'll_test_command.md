```sh
# 🔤 String Tests
[ -z "$str" ]       # True if string is empty
[ -n "$str" ]       # True if string is NOT empty
[ "$a" = "$b" ]     # True if strings are equal
[ "$a" != "$b" ]    # True if strings are not equal

# 🔢 Number Tests
[ "$a" -eq "$b" ]   # Equal
[ "$a" -ne "$b" ]   # Not equal
[ "$a" -lt "$b" ]   # Less than
[ "$a" -le "$b" ]   # Less than or equal
[ "$a" -gt "$b" ]   # Greater than
[ "$a" -ge "$b" ]   # Greater than or equal

# 📁 File Tests
[ -e "$file" ]      # File exists (any type)
[ -f "$file" ]      # File is a regular file
[ -d "$dir" ]       # File is a directory
[ -r "$file" ]      # File is readable
[ -w "$file" ]      # File is writable
[ -x "$file" ]      # File is executable
[ -s "$file" ]      # File exists and size > 0

# 🔄 Combining Conditions
[ "$a" -gt 5 ] && echo "a is greater than 5"
[ -f "$f" ] || echo "File not found"

# ✅ With if
if [ "$a" = "yes" ]; then
  echo "Confirmed"
fi

# 🔁 Multiple Conditions (POSIX style)
if [ "$a" -gt 0 ] && [ "$b" -gt 0 ]; then
  echo "Both are positive"
fi 