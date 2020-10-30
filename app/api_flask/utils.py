# -*- coding: utf-8 -*-
import inspect

from flask.blueprints import Blueprint
from werkzeug.utils import find_modules, import_string


def register_blueprints(app, root='views'):
    """自动注册蓝图"""

    base_len = len(root.split('.'))

    for mod_name in find_modules(root, recursive=True):
        mod = import_string(mod_name)
        prefix = '/' + '/'.join(mod_name.split('.')[base_len:])

        for instance_name, clazz in inspect.getmembers(mod, predicate=lambda x: isinstance(x, Blueprint)):
            instance = getattr(mod, instance_name)
            app.register_blueprint(instance, url_prefix=prefix)
