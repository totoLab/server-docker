import json

with open("config.json", "r") as f:
    d = json.load(f)

domain = "antolab.net"
website = d[domain]
headers = website["headers"]
hosts = d["hosts"]
rules = website["rules"]
domain = "{$DOMAIN}"
ssl_directive = "import tls_config"
urls = ""
for host in rules:
    subdomains = rules[host]
    
    for subdomain in sorted(subdomains):
        urls += subdomain + f"{"." if subdomain != "" else ""}" + f"{domain} "

    hostname, port = host.split(":")
    ip = hosts[hostname]
    new_host = f"{ip}:{port}"
    urls += "{" f"\n\t{ssl_directive}\n\treverse_proxy {new_host}\n" + "}\n\n"

redirections = website["redirection"]
for new_url in redirections:
    subdomains = redirections[new_url]
    for subdomain in sorted(subdomains):
        urls += subdomain + f"{"." if subdomain != "" else ""}" + f"{domain} "

    urls += "{" f"\n\t{ssl_directive}\n\tredir {new_url} permanent\n" + "}\n\n"

content = ""
for header in headers:
    content += f"{header}\n\n"

content += urls

with open("Caddyfile", "w") as f:
    f.write(content)
