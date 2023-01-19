# plex-scripts

## IP Updater

This directory contains the scripts that solve the problem of using dynamic IPs in the Nginx `proxy_pass` configuration. The scripts allow the remote host to keep up to date on what the Plex server's IP address is, and will automatically update the Nginx configuration to always point to the right IP.
