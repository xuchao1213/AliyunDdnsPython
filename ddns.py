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
    print ("agr len :" + str(len(sys.argv)))
    print(str(sys.argv[0]))

    local_ip = Util.getLocalInternetIp()
    if local_ip[0] is False:
        print local_ip[1]
        return
    """
    //TODO 更新IP
    """


if __name__ == "__main__":
    main()
