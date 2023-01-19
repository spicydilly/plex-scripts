# IP Updater Remote Server

This script checks if the local file storing the IP of the home server has been updated. If it has been updated it will update Nginx config and reload. The remote host with Nginx uses `proxy_pass` to redirect an address to the Plex server's IP. For example, [tautulli.thedylon.com](https://tautullu.thedylon.com) would redirect to the Tautulli host setup on the Plex server.

## Prerequisites

This script is intended to be run on Ubuntu.

- `inotifytools`, install using the following command:

```sh
sudo apt update
sudo apt install inotify-tools
```

## Set-Up

1. Copy the contents of the [remote-server](/ip-updater/remote-server/) directory to the remote server at `/root/home-ip/`.
2. Create the system service:

    ```sh
    nano /etc/systemd/system/check-ip.service
    ```

3. Insert the following:

    ```conf
    [Unit]
    Description=Checks if Plex server IP has changed.

    [Service]
    User=root
    ExecStart=/bin/bash /root/home-ip/check-ip-update.sh

    [Install]
    WantedBy=multi-user.target
    ```

4. Reload `systemd` with this command:

    ```sh
    systemctl daemon-reload
    ```

5. Enable the service using:

    ```sh
    systemctl enable check-ip.service
    ```

6. Start the service using:

    ```sh
    systemctl start check-ip.service
    ```
