# TelegramRunAway
Auto delete all your messages in all group chat

## Install requirements
pip3 install -U pyrogram tgcrypto

## Setup API
sign into https://my.telegram.org/apps and get your api id and hash

## Modify
fill your api id and hash in main.py

## Run
just run it

## cronjob
try something like this on a server
```
0 0 * * * /usr/bin/python3 /TelegramRunAway/main.py
```

