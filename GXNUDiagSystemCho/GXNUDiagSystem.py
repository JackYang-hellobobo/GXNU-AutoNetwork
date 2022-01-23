# -*- coding:utf-8 -*-
from urllib.request import Request
import urllib.request
import urllib.parse
from socket import *
from http.cookiejar import CookieJar
import re
from Config import Config
import requests


class GXNUDiagSystem:
    def __init__(self):
        self.config = Config()
        self.config = self.config.getConfig()
        self.usrname = self.config['username']
        self.passwd = self.config['password']
        self.type = self.config['type']
        self.cookiejar = CookieJar()
        self.browser = urllib.request.HTTPCookieProcessor(self.cookiejar)
        self.browser = urllib.request.build_opener(self.browser)
        self.conStatus, self.exception = self.checkConnection()
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.aliveStatus = self.checkAlive()

    def checkConnection(self):
        try:
            self.browser.open(self.config['host'])
            return True, ''
        except Exception as e:
            return False, str(e)

    def checkAlive(self):
        try:
            baidu_html = requests.get("https://www.baidu.com", timeout=2)
            qq_html = requests.get("https://www.qq.com", timeout=2)
            bilibli_html = requests.get("https://www.bilibili.com", timeout=2)
        except:
            return False
        return True

    def generatePostData(self):
        data = {
            'DDDDD': self.usrname,
            'upass': self.passwd,
            'R1': '0',
            'R2': '',
            'R3': self.type,
            'R6': '0',
            'para': '00',
            'OMKKEY': '123456',
            'buttonClicked': '',
            'redirect_url': '',
            'err_flag': '',
            'username': '',
            'password': '',
            'user': '',
            'cmd': '',
            'Login': '',
        }
        return urllib.parse.urlencode(data).encode('utf-8')

    def login(self):
        # if not self.conStatus:
        #     print('连接未初始化，请检查网络连接是否正常')
        #     return False
        # if self.aliveStatus:
        #     print('网络已连接，请勿重复操作')
        #     return True
        post = self.generatePostData()
        request = Request(self.config['loginpage'], post)
        response = self.browser.open(request)
        html = response.read()
        pattern = r'<title>认证成功页</title>'
        obj = re.compile(pattern)
        flag = len(obj.findall(html.decode('gb2312')))
        if flag == 1:  # 这里是判断网络是否连接成功
            return True
        return False

    def logout(self):
        if not self.conStatus:
            print('连接未初始化，请检查网络连接是否正常')
            return False
        response = self.browser.open(self.config['logoutpage'])
        html = response.read()
