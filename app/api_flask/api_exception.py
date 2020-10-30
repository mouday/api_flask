# -*- coding: utf-8 -*-


class ApiException(Exception):
    """自定义异常"""

    def __init__(self, msg, code=-1):
        self.msg = msg
        self.code = code

    def __str__(self):
        return self.msg
