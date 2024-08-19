# Architecture
Server is currently
- a RPi4 2GB
- an old x86_64 laptop
with both machines running Ubuntu Server. All images and containers are tested on ARM64 architecture, except for Immich, running on x86_64.

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