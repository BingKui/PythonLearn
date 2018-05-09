# 这个一部分会学习如何建立一个完整的项目“骨架”
# 其中包含：项目布局文件、自动化测试代码、模组以及安装脚本
# 当建立一个新项目时，只用复制目录结构，修改项目名称，再编辑里边的文件就行了

# 骨架内容
# workspace(工作目录)
#   |-ProjectName
#   |    |-bin
#   |    |-NAME(项目猪文件夹，可随意命名)
#   |    |  |-__init__.py
#   |    |-tests
#   |    |  |-__init__.py
#   |    |-docs
#   |    |-setup.py


# setup.py
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python项目骨架搭建示例',
    'author': '康兵奎',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)

# 测试专用的骨架文件
# tests/NAME_tests.py
from nose.tools import *
import NAME

def setup():
    print "setup"

def teardown():
    print "Tear Down!"

def test_basic():
    print "I ran!"


# python 软件包安装

# 安装软件
# 1.pip
# 2.nose
# 3.distribute
# 4.virtualenv

# 安装过程可能需要使用 sudo 命令，提高用户权限
