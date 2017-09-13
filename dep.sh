#!/bin/bash

# install python
apt-get update |apt-get install python python-pip

#stop exit service
systemctl stop ddns
systemctl disable ddns

# remove exist file
rm -r /opt/AliyunDdnsPython
rm /usr/lib/systemd/system/ddns.service

#install dependence
pip install --upgrade pip
pip install requests
pip install aliyun-python-sdk-core
pip install aliyun-python-sdk-alidns

# copy file to /opt/AliyunDdnsPython
mkdir -p /opt/AliyunDdnsPython
cp *.* /opt/AliyunDdnsPython/

# install service and run
mkdir -p /usr/lib/systemd/system
cp ddns.service /usr/lib/systemd/system/ddns.service
systemctl daemon-reload
systemctl enable ddns
systemctl start ddns

