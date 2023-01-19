# IP Updater Home Server

This script uses [https://wtfismyip.com](https://wtfismyip.com) to fetch the Plex server's IP address, and if a change in IP is detected it uses the [pscp provided by PUTTY](https://www.putty.org/) to sync the file to a remote host.

## Prerequisites

This script is intended to be run on Windows.

- [Python3](https://www.python.org/downloads/)
- [Putty](https://www.putty.org/)

## Set Up Scheduled Task

1. Copy the contents of the [home-server](/ip-updater/home-server/) directory to the Plex server.
2. Add the IP of the remote host to [remote-ip.conf](/ip-updater/home-server/config/remote-ip.conf).
3. Add the root password for the remote host to [pw.conf](/ip-updater/home-server/config/pw.conf).
4. Add the paths to `python.exe` and `ip-updater.py` to [ip-task.bat](/ip-updater/home-server/ip-task.bat).
5. Search for `Task Scheduler` on windows and open it.
6. Choose the option to ‘Create Basic Task…’.
7. Type a name for the task, and then press `Next`.
8. Choose to start the task ‘Daily‘ at any time.
9. Select, `Start a program,` and then press `Next`.
10. Use the `Browse` button to find the batch file `ip-task.bat`.
11. Click on `Finish`.
12. Double-click on the newly created task, and select the `Triggers` tab.
13. Double-click on the daily trigger, and under `Advanced Settings` you can set the task to run every `x` minutes.
