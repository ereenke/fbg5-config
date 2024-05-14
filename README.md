# Flyingbear Ghost 5 config backup 💾
These steps need to be taken to restore my config in case microSD card breaks again.

### MainsailOS
Install MainsailOS.

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

/klipper-backup/.env
```shell

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

Manual run:
```shell
~/klipper-backup/script.sh
```


