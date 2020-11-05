# _*_coding=utf-8 _*_
# @author zhangsanga
# @date 2020/11/5 15:06
from flask import Blueprint
from flask_restful import Api


# app
# 作用:路由分组，1.使用统一前缀 2.使用统一view层（前后端分离不需要）
blog_app = Blueprint('blogapp', __name__)
blog_api = Api(blog_app)
