#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from sdkwrapper import AliYunSdkWrapper
from util import Util


def main():
    """
    Main Function
    """
    print "ali-ddns run ..."
    local_ip = Util.getLocalInternetIp()
    if local_ip[0] is False:
        print local_ip[1]
        return
    """
    load config ,init AliYunSdkWrapper
    """
    print "local ip " + local_ip
    sdkUtil = AliYunSdkWrapper(
        "access_key_id",
        "access_key_secret",
        "domain_name",
        "sub_domain_name",
        "A",
        "cn-hangzhou"
    )
    """
   update the record
    """
    res = sdkUtil.getRecordValue()
    if res[0]:
        sdkUtil.setRecordValue(local_ip[1])
    else:
        print res[1] + "[Skip]"

if __name__ == "__main__":
    main()
