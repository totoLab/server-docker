# Architecture
Server is currently
1. network hub (RPi4 - 2GB ram)
2. main server + NAS (HP elitedesk - 16GB ram)

<br>
NAS capabilities is achieved with a 2 disk software RAID (using laptop hard disks hooked through a docking station). 

# Services
RPi4 acts as a networking hub, for managing and  monitoring the network. Both instances have glances ("web htop") for monitoring resources.

## Network hub (1)
- [x] portainer (main)
- [x] nginx-proxy-manager (reverse proxy)
- [x] cloudflare-ddns
- [ ] pi-hole 
- [x] upsnap (WOL)
- [x] uptime-kuma
- [x] nginx (websites)
- [x] wireguard/tailscale (VPN)
- [x] motioneye

## Main server (2)
[!WARNING]
This machine will be managed through a docker agent from 

- [x] immich
- [ ] vaultwarden
- [x] navidrome
- [x] plex/jellyfin
- [x] paperless ngx
- [x] filebrowser
- [x] kavita
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
