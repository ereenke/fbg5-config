# Flyingbear Ghost 5 config backup 💾
These steps need to be taken to restore my config in case microSD card dead again.

### Install MainsailOS

https://docs-os.mainsail.xyz/


### Setting RPi as a secondary MCU
Will be needed to connect the ADXL345 sensor and macro buttons.

https://www.klipper3d.org/RPi_microcontroller.html

Install the rc script:
```shell
cd ~/klipper/
sudo cp ./scripts/klipper-mcu.service /etc/systemd/system/
sudo systemctl enable klipper-mcu.service
```

```
cd ~/klipper/
make menuconfig
```
In the menu, set "Microcontroller Architecture" to "Linux process," then save and exit.

```shell
sudo service klipper stop
make flash
sudo service klipper start

sudo usermod -a -G tty pi
```
### Increasing the MCU temperature alarm limit
From 60C default to 70C.
```shell
sudo nano /boot/config.txt

[all]
temp_soft_limit=70
```

### G-Code Shell Command Plugin
```shell
sudo apt-get update && sudo apt-get install git -y

cd ~ && git clone https://github.com/dw-0/kiauh.git
```

```shell
./kiauh/kiauh.sh

4. Advanced -> 8. G-Code Shell Command
```

### Klipper-Backup
Klipper backup script for manual or automated GitHub backups.

https://klipperbackup.xyz/

```shell
curl -fsSL get.klipperbackup.xyz | bash
~/klipper-backup/install.sh
```

```shell
nano /klipper-backup/.env

github_token=
github_username=ereenke
github_repository=fbg5-config
branch_name=main
commit_username="user"
commit_email="user@3dprinter"

backupPaths=( \
"printer_data/config/*" \
"printer_data/database/*" \
)
```

```shell
sudo nano /etc/systemd/system/github-backup.service

[Unit]
Description="Github backup service"
After=network-online.target

[Service]
ExecStart=/home/user/klipper-backup/script.sh

[Service]
User=user
Type=oneshot
ExecStart=/usr/bin/env bash  -c "/usr/bin/env bash $HOME/klipper-backup/script.sh \"New Backup - $(date +\"%%x - %%X\")\""
#ExecStart=/bin/bash -c 'bash $HOME/klipper-backup/script.sh'

[Install]
WantedBy=default.target
```

```shell
sudo nano /etc/systemd/system/github-backup.timer


[Unit]
Description="Github backup timer"

[Timer]
OnCalendar=weekly
Persistent=true
Unit=github-backup.service

[Install]
WantedBy=multi-user.target
```

```shell
sudo systemctl start github-backup.service
sudo systemctl enable github-backup.service
```

Manual run:
```shell
~/klipper-backup/script.sh
```
