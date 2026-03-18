TO link codespace

do this : 
gh codespace ssh --config > ~/.ssh/codespaces

then write this in ~/.ssh/config:
printf 'Match all\n  Include ~/.ssh/codespaces\n' >> ~/.ssh/config


to link codespace ssh for easy access
