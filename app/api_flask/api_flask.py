# -*- coding: utf-8 -*-
from flask import Flask, jsonify

from app.api_flask.api_exception import ApiException
from app.api_flask.api_json_encoder import ApiJSONEncoder
from app.api_flask.api_request import ApiRequest
from app.api_flask.api_result import ApiResult


class ApiFlask(Flask):
    """
    参考
    Flask最佳实践
    https://zhuanlan.zhihu.com/p/22774028
    """
    request_class = ApiRequest

    json_encoder = ApiJSONEncoder

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('static_folder', None)
        super().__init__(*args, **kwargs)
        self._register_error_handler(None, Exception, self.error_handler)

    def make_response(self, rv):
        """视图函数可以直接返回list 或者 dict"""

        if not isinstance(rv, ApiResult):
            rv = ApiResult.success(rv)

        return jsonify(rv)

    def error_handler(self, exception):
        """统一处理异常"""

        if isinstance(exception, ApiException):
            code = exception.code
            msg = str(exception)
        else:
            code = -1
            msg = '未知错误'

        return ApiResult.failure(None, msg, code)
