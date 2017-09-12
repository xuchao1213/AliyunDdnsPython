#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from sdkwrapper import AliYunSdkWrapper
from util import Util
from config import Config

CONFIG_FILE = "ddns.conf.example"


def main():
    """
    Main Function
    """
    print "ali-ddns run ..."
    """
    load config 
    """
    ddnsConfig = Config()
    loadRes = ddnsConfig.loadConfig(CONFIG_FILE)
    if loadRes:
        """
        get current local internet ip
        """
        local_ip = Util.getLocalInternetIp()
        if local_ip[0] is False:
            print local_ip[1]
            return
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
        res = sdkUtil.getRecordValue()
        if res[0]:
            sdkUtil.setRecordValue(local_ip[1])
        else:
            print res[1] + "[Skip]"


if __name__ == "__main__":
    main()
