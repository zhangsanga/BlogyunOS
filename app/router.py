# _*_coding=utf-8 _*_
# @author zhangsanga
# @date 2020/11/4 15:39
import os
from flask import Flask
from flask_session import Session
from app.pkg.database.redis_db.client import RedisTool
from app.blog.router import blog_app

class Service(object):
    def __init__(self):
        self._app = Flask('test_api', instance_relative_config=True)
        self.set_session()
        self.add_app()

    # 添加路由分组
    def add_app(self):
        # 添加特征提取分组
        self._app.register_blueprint(
            blog_app, url_prefix='/blog'
        )

    # 添加session设置
    def set_session(self):
        self._app.secret_key = os.urandom(24)
        self._app.config['SESSION_COOKIE_NAME'] = 'portrait_platform'
        self._app.config['SESSION_TYPE'] = 'redis'
        self._app.config['SESSION_REDIS'] = RedisTool().get_client()
        self._app.config['SESSION_PERMANENT'] = True
        self._app.config['PERMANENT_SESSION_LIFETIME'] = 86400
        self._app.config['SESSION_COOKIE_HTTPONLY'] = False
        Session(self._app)

    def get_app(self):
        return self._app


service = Service()
