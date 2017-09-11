#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests


class Util:
    def __init__(self):
        pass

    @classmethod
    def getLocalInternetIp(cls):
        try:
            res = requests.get("http://ip.3322.net")
        except requests.RequestException as ex:
            return False, "Get Local Internet Ip Error (" + ex.message + ")"

        if res.status_code != requests.codes.ok:
            return False, "Get Local Internet Ip Failed (Http code :" + res.status_code + ", message :" + res.content + ")"

        return True, res.content.decode('utf-8').rstrip("\n")
