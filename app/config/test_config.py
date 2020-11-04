# _*_coding=utf-8 _*_
# @author zhangsanga
# @date 2020/11/4 16:19

import os
import configparser

conf_path = '{}/smart_up.conf'.format(os.environ.get('PWD', '/home/www/BlogyunOS'))

def read_conf():
    config = configparser.ConfigParser()
    try:
        config.read(conf_path)
        return config
    except:
        raise Exception('read config file failed! default path: %s' % conf_path)


config_file = read_conf()