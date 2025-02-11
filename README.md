# Architecture
Server is currently
1. network hub (RPi4 - 2GB ram)
2. main server + NAS (HP elitedesk - 16GB ram)

<br>
NAS capabilities is achieved with a 2 disk software RAID (using laptop hard disks hooked through a docking station). 

# Services
RPi4 acts as a networking hub, for managing and  monitoring the network. Every machine runs a `backrest` container for backups to multiple locations and `glances` for monitoring.

## Network hub (1)
- [x] portainer (main)
- [x] caddy (reverse proxy)
- [x] cloudflare-ddns
- [ ] pi-hole 
- [x] upsnap (WOL)
- [x] uptime-kuma
- [x] nginx (websites)
- [x] wireguard/tailscale (VPN)
- [x] motioneye

## Main server (2)
> [!WARNING]  
> This machine will be managed through a docker agent from the [Network Hub](#network-hub-1)

- [x] immich
- [ ] vaultwarden
- [x] navidrome
- [x] plex/jellyfin
- [x] paperless ngx
- [x] filebrowser
- [x] kavita
- [x] minecraft free server
- [x] metube (content downloader)
- [ ] audiobookshelf
- [ ] addy.io

# Prerequisites
```
docker
```

# Usage
Almost all containers need some sort of configuration in the form of a .env or .json file. Then 
```
cd server-docker/myservice && docker compose up -d 
```

# Extra
For my terminal I use these [dotfiles](https://github.com/totoLab/dotfiles).
