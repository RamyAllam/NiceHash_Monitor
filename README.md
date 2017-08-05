# Nicehash Monitor - Beta 0.1
## Intro
Nicehash Monitor is a python script to monitor running workers through NiceHash API. Using this script you will get email and telegram notifications for down workers and will restart Window automatically if the worker is down.

This script supports two types of monitors as follow:
- Remote Monitoring

In this mode, you will run the monitor on a dedicated/separate machine where it monitors the running workers and sends you the notifications in case of failures. This mode can run on any Linux or Windows machine which supports the below requirements.

- Local Monitoring

In this mode, You will run the monitor on the same Windows machine that runs NiceHash miner software. It does the same job of the remote monitor plus it has the feature to reboot the Windows machine if worker is down in case of any failures or crashes such the common GPU crashes.

Best practice is to run both remote and local monitoring.

## Requirements
### Modify variables
- With any files editor, modify the variables in vars.py file

### Linux
#### - Python Installation
- yum -y install yum-utils
- yum -y groupinstall development
- yum -y install https://centos6.iuscommunity.org/ius-release.rpm
- yum -y install python35u
- yum -y install python35u-pip
- pip3 install requests
- echo 'alias python3="python3.5"' >> /etc/bashrc
- echo 'alias pip3="pip3.5"' >> /etc/bashrc
- alias python3="python3.5"
- alias pip3="pip3.5"

### Windows
#### - Python Installation
- Download and Install Python from : https://www.python.org/downloads/windows/

---
## Execution
### Remote Monitoring - Linux
#### 1. Start Process
- Set `monitor_type` in vars.py file to `server_end`
- cd /path/to/script/ ; while true ; do python3 main.py ; done

#### 2. Run On Startup
- echo 'cd /path/to/script/ ; while true ; do python3 main.py ; done' > /root/start_monitor.sh
- echo 'sh /root/start_monitor.sh &' >> /etc/rc.local
- chmod +x /etc/rc.local

### Remote Monitoring - Windows
#### 1. Start Process
- Set `monitor_type` in vars.py file to `server_end`
- Run `main.py` file

#### 2. Run On Startup
- Follow this please : https://goo.gl/tu4pK3

### Local Monitoring - Windows
#### 1. Start Process
- Set `monitor_type` in vars.py file to `miner_end`
- Run `main.py` file

#### 2. Run On Startup
- Follow this please : https://goo.gl/tu4pK3

---
## References
- Create Telegram bot : https://goo.gl/tJ9H9t
- How to get Telegram ChatID : https://goo.gl/Rru7N8
- Telegram bot youtube tutorial : https://goo.gl/LeJ7HQ , https://goo.gl/3V2Sy4
- Gmail SMTP SSL : https://goo.gl/JQ9Mcz
- Yahoo SMTP SSL : https://goo.gl/gYqXn1
- Outlook SMTP SSL : https://goo.gl/3w2mwr
- Zoho SMTP SSL : https://goo.gl/TWqkf4
- Amazon SES SMTP SSL : https://goo.gl/N2hxjC
- Gmail less secure apps : https://goo.gl/2brG9P

#### Cloud for remote monitoring
- https://m.do.co/c/b17c2d7a505f
- https://aws.amazon.com/ec2/
- https://www.linode.com/
- https://cloud.google.com/compute/
- https://azure.microsoft.com/en-us/

---
## Donation
Like it? Share your support!
- BTC  : 1BkoHW3KF8E7qmUQ1xgpfPVd7BokEGozoQ
- LTC  : LYCf7Snnk8fA3coNFbVmCZtu3CLJWG3AP2
- ETH  : 0x75373d2cb5f89d3f35cd7426659e2741a8044a0e
- ZEC  : t1TBpHvUSGeXaPsfTjPdRgjT7qqVHijVw1F
- DOGE : DC6aT3Z2wPUFxaqQbJefYczV37GvQURtm3