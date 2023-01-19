inotifywait -q -m -e close_write /root/home-ip/home-ip.conf |
while read -r filename event; do
  export PLEX_URL=$(cat /root/home-ip/home-ip.conf)
  envsubst '${PLEX_URL}' < /root/home-ip/plex.thedylon.com.template > /etc/nginx/sites-available/plex.thedylon.com
  sudo systemctl restart nginx.service
done
