# -*- coding: utf-8 -*-
from flask import Request


class ApiRequest(Request):

    @property
    def json(self):
        """避免json数据未传递而返回 None"""
        try:
            data = self.get_json()
        except Exception as e:
            data = None

        return data or {}
