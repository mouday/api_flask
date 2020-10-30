# -*- coding: utf-8 -*-
from flask.blueprints import Blueprint


class ApiBlueprint(Blueprint):

    """扩展蓝图"""
    def mapping(self, rule, **options):
        options.setdefault('methods', ['GET', 'POST'])
        return self.route(rule, **options)

    def get(self, rule, **options):
        options.setdefault('methods', ['GET'])
        return self.route(rule, **options)

    def post(self, rule, **options):
        options.setdefault('methods', ['POST'])
        return self.route(rule, **options)
