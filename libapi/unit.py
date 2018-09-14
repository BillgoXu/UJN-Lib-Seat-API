#!/usr/bin/env python
# encoding: utf-8

import json

class LoginException(BaseException):
    def __init__(self, account, password, message):
        err = '登录异常:账号:%s 密码:%s %s' % (account, password, message)
        BaseException.__init__(self, err)
        self.err = err
        self.account = account
        self.password = password
        self.message = message

class ParseJsonException(BaseException):
    def __init__(self, s):
        err = "parse str into json dict error, {} is not json".format(s)
        BaseException.__init__(self, err)


class JsonDict(dict):
    def __init__(self, *args, **kwargs):
        super(JsonDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

    def __str__(self):
        return json.dumps(self, encoding="utf-8", ensure_ascii=False, indent=2).encode('utf-8')


def parse_json(json_str):
    """parse str into JsonDict"""
    try:
        return json.loads(json_str, object_hook=JsonDict)
    except:
        raise ParseJsonException(json_str)