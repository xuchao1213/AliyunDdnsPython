#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

if sys.version_info < (3,):
    import ConfigParser
else:
    import configparser as ConfigParser


class Config:
    def __init__(self):
        self.interval = 30
        self.access_key_id = None
        self.access_key_secret = None
        self.domain_name = None
        self.sub_domain_name = None
        self.record_type = "A"
        self.region_id = "cn-hangzhou"

        self.configParser = ConfigParser.ConfigParser()

    def loadConfig(self, file):
        if not self.configParser.read(file):
            print "config file not exist"
            return False
        try:
            self.interval = self.configParser.getint("CONFIG", "interval")
            self.access_key_id = self.configParser.get("CONFIG", "access_key_id")
            self.access_key_secret = self.configParser.get("CONFIG", "access_key_secret")
            self.domain_name = self.configParser.get("CONFIG", "domain_name")
            self.sub_domain_name = self.configParser.get("CONFIG", "sub_domain_name")
            self.record_type = self.configParser.get("CONFIG", "record_type")
            self.region_id = self.configParser.get("CONFIG", "region_id")
            if not self.interval:
                self.interval = 30
            if not self.record_type:
                self.record_type = "A"
            if not self.region_id:
                self.region_id = "cn-hangzhou"
        except Exception, e:
            print "invalid config: {0}".format(e.message)
            return False

        if not self.access_key_id or not self.access_key_secret or not self.domain_name or not self.sub_domain_name:
            print "invalid config"
            return False

        return True
