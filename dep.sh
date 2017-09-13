#!/bin/bash

# install python
apt-get update |apt-get install python python-pip

#install dependence
pip install requests
pip install aliyun-python-sdk-core
pip install aliyun-python-sdk-alidns

# copy file to /opt/AliyunDdnsPython
cp *.* /opt/AliyunDdnsPython/

# install service and run
cp ddns.service /usr/lib/systemd/system/
systemctl daemon-reload
systemctl enable ddns
systemctl start ddns

