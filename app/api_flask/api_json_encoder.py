# -*- coding: utf-8 -*-
from flask.json import JSONEncoder

from app.api_flask.api_result import ApiResult


class ApiJSONEncoder(JSONEncoder):
    """格式化json"""

    def default(self, obj):
        if isinstance(obj, ApiResult):
            return obj.to_dict()
        else:
            return JSONEncoder.default(self, obj)
