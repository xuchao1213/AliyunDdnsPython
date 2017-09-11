#!/usr/bin/python
# -*- coding: utf-8 -*-

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
from aliyunsdkalidns.request.v20150109.AddDomainRecordRequest import AddDomainRecordRequest
import json


class AliYunSdkWrapper:
    """
    Wrapper of AliYun Python Sdk
    """

    def __init__(self,
                 access_key_id,
                 access_key_secret,
                 domain_name,
                 sub_domain_name,
                 record_type="A",
                 region_id="cn-hangzhou"):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.region_id = region_id
        self.domain_name = domain_name
        self.sub_domain_name = sub_domain_name
        self.record_type = record_type
        self.record_id = ""
        self.remote_record_value = ""
        self.has_remote_record = False
        self.client = AcsClient(
            access_key_id,
            access_key_secret,
            region_id
        );

    def getRecordValue(self):
        self.__requireParmSet()
        # create request and set parm
        request = DescribeDomainRecordsRequest()
        request.set_DomainName(self.domain_name)
        request.set_TypeKeyWord(self.record_type)
        request.set_RRKeyWord(self.sub_domain_name)
        # execute
        res = self.__tryExecute(request)
        if res[0]:
            print "ok: " + res[1]
            resJsonObj = json.loads(res[1])
            for record in resJsonObj["DomainRecords"]["Record"]:
                if record["RR"] == self.sub_domain_name:
                    self.has_remote_record = True
                    self.record_id = record["RecordId"]
                    self.remote_record_value = record["Value"]
                    return True, record["Value"]
            self.has_remote_record = False
            self.record_id = ""
            self.remote_record_value = ""
            return True, None
        else:
            print "error: " + res[1]
            return res

    def setRecordValue(self, record_value):
        self.__requireParmSet()
        # creat request，set parm
        if self.has_remote_record:
            if record_value == self.remote_record_value:
                print "current local internet ip is " + record_value + ", which same as the remote record [SKIP]"
                return True
            else:
                print "current local internet ip is " + record_value + ", which different from the remote record " + self.remote_record_value + " [UPDATE]"
                request = UpdateDomainRecordRequest()
                request.set_RecordId(self.record_id)
                request.set_RR(self.sub_domain_name)
                request.set_Type(self.record_type)
                request.set_Value(record_value)
        else:
            print "current local internet ip is " + record_value + ", the remote sub domain record do not exist ! [ADD]"
            request = AddDomainRecordRequest()
            request.set_DomainName(self.domain_name)
            request.set_RR(self.sub_domain_name)
            request.set_Type(self.record_type)
            request.set_Value(record_value)
        # execute
        res = self.__tryExecute(request)
        if res[0]:
            if self.has_remote_record:
                print "update [OK]"
            else:
                print "add [OK]"
        else:
            if self.has_remote_record:
                print "update [ERROR] " + res[1]
            else:
                print "add [ERROR] " + res[1]

    def __requireParmSet(self):
        if self.access_key_id is None or self.access_key_id.strip() == '':
            raise Exception("invalid access_key_id !", self.domain_name)
        if self.access_key_secret is None or self.access_key_secret.strip() == '':
            raise Exception("invalid access_key_secret !", self.sub_domain_name)
        if self.domain_name is None or self.domain_name.strip() == '':
            raise Exception("invalid domain_name !", self.domain_name)
        if self.sub_domain_name is None or self.sub_domain_name.strip() == '':
            raise Exception("invalid sub domain_name !", self.sub_domain_name)
        if self.record_type is None or self.record_type.strip() == '':
            self.record_type = "A"
        if self.region_id is None or self.region_id.strip() == '':
            self.region_id = "cn-hangzhou"

    def __tryExecute(self, request):
        request.set_accept_format("json")
        try:
            response = self.client.do_action_with_exception(request)
            return True, response
        except ClientException, e:
            return False, "client error :" + e.message
        except ServerException, e:
            return False, "server error :" + e.message
        except Exception, e:
            return False, "error :" + e.message
