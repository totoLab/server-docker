cat <<EOF | docker exec --interactive caddy sh
caddy validate --config /etc/caddy/Caddyfile && caddy reload --config /etc/caddy/Caddyfile || echo "Something wrong with current config"; exit 1;
EOF
