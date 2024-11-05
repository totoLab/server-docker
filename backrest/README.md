# External script for Telegram Notifications
Needed to version control the script without copying/pasting.

## Setup

Set environment variable in `.env` file:
```
TG="/root/scripts/tg_notify.sh"
```
this file on host has to be in the corresponding directory mounted in `docker-compose.yml`, then in Backrest's hook section execute the script at that location (can also pass parameters):
```
. "$TG" "{{ .Plan.Id }}" "{{ .Summary }}"
```
