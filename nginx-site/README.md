# nginx-site 
Main webserver configuration: docker + nginx (custom config), hosting multiple sites, specified in "nginx.conf".

## running
Config file specifies individual servers, running the nginx-dockerSetup script will docker-compose the container placing the config file in the filesystem and restarting the container.

## sites
If specified in the config file as servers and present in the folder mounted in the docker-compose.yml websites will be available (given that domains/subdomains are accessible). 

Current are:
- antolab.xyz (main)
- miao.@      (test subdomain)
