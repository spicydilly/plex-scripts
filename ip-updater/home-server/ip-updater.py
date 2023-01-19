"""
This script fetches the IP of the machine, and if a change is detected
    using pscp to update the IP on server
"""

import urllib.request
import subprocess
import os


script_dir = os.path.dirname(os.path.realpath(__file__))
pw_file = f"{script_dir}\\config\\pw.conf"
home_ip_file = f"{script_dir}\\config\\home-ip.conf"
remote_ip_file = f"{script_dir}\\config\\remote-ip.conf"


def get_ip():
    """Gets IP of PC"""
    url = "https://wtfismyip.com/text"
    ip = urllib.request.urlopen(url).read().decode("utf-8").strip()
    return ip


def check_if_ip_changed(ip):
    """Checks if IP has changed from last update"""
    with open(home_ip_file, "r", encoding="utf-8") as f:
        for line in f:
            if line == ip:
                return False
    return True


def update_ip(ip):
    """Updates file & server with new IP"""
    # get ip of remote server
    remote_ip = ""
    with open(remote_ip_file, "r", encoding="utf-8") as f:
        for line in f:
            remote_ip = line
    if remote_ip:
        with open(home_ip_file, "w", encoding="utf-8") as f:
            f.write(ip)

        subprocess.run(["pscp", "-pwfile", pw_file, home_ip_file,
                        f"root@{remote_ip}:/root/home-ip/"], check=False)


ip = get_ip()
if check_if_ip_changed(ip):
    update_ip(ip)
