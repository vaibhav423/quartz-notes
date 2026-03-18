
# Essential Termux Session Commands

if u remove no-shell-with-name , it will create duplicate if alread one exists
## Create or Focus a Session
If the session name exists, it switches to it; otherwise, it creates it.
```bash
am startservice --user 0 -n com.termux/com.termux.app.RunCommandService \
-a com.termux.RUN_COMMAND \
--es com.termux.RUN_COMMAND_PATH '/data/data/com.termux/files/usr/bin/zsh'\
--esa com.termux.RUN_COMMAND_ARGUMENTS '-c,yazi' \
--es com.termux.RUN_COMMAND_SHELL_NAME "yazi-explorer" \
--es com.termux.RUN_COMMAND_SHELL_CREATE_MODE "no-shell-with-name"
```
## Run a Command in a New Session in background in shell , it wont show session in tabs

```bash
am startservice --user 0 -n com.termux/com.termux.app.RunCommandService \
-a com.termux.RUN_COMMAND \
--es com.termux.RUN_COMMAND_PATH '/data/data/com.termux/files/usr/bin/top' \
--esa com.termux.RUN_COMMAND_ARGUMENTS '-n,5' \
--es com.termux.RUN_COMMAND_SHELL_NAME "monitor-task" \
--es com.termux.RUN_COMMAND_SHELL_CREATE_MODE 'no-shell-with-name' \
--es com.termux.RUN_COMMAND_RUNNER "app-shell"
```
## to reopen a named session

rum the command again , runcommand path is madnatory but it can be anything
as it wont be used if session already exists

```bash
am startservice --user 0 -n com.termux/com.termux.app.RunCommandService \
-a com.termux.RUN_COMMAND \
--es com.termux.RUN_COMMAND_PATH '/data/data/com.termux/files/usr/bin/zsh'\
--esa com.termux.RUN_COMMAND_ARGUMENTS '-c,yazi' \
--es com.termux.RUN_COMMAND_SHELL_NAME "yazi-explorer" \
--es com.termux.RUN_COMMAND_SHELL_CREATE_MODE "no-shell-with-name"
```

[[ run]]
