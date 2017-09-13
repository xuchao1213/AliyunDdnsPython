#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading

from sdkwrapper import AliYunSdkWrapper
from util import Util
from config import Config

CONFIG_FILE = "ddns.conf"


def main():
    """
    Main Function
    """
    """
    load config 
    """
    ddnsConfig = Config()
    if ddnsConfig.loadConfig(CONFIG_FILE):
        """
        get current local internet ip
        """
        local_ip = Util.getLocalInternetIp()
        if local_ip[0]:
            """
            init AliYunSdkWrapper
            """
            sdkUtil = AliYunSdkWrapper(
                ddnsConfig.access_key_id,
                ddnsConfig.access_key_secret,
                ddnsConfig.domain_name,
                ddnsConfig.sub_domain_name,
                ddnsConfig.record_type,
                ddnsConfig.region_id
            )
            """
            update record
            """
            sdkUtil.updateRecord(local_ip[1])
            scheduleTimerTask(ddnsConfig.interval * 60)
        else:
            print local_ip[1]
            scheduleTimerTask(ddnsConfig.interval * 60)
    else:
        print "not config yet , retry 1 min later...... 【Skip】"
        scheduleTimerTask(1 * 60)


def scheduleTimerTask(interval):
    timer = threading.Timer(interval, main)
    timer.start()


if __name__ == "__main__":
    print "ali-ddns run ..."
    scheduleTimerTask(3)
