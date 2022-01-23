# -*- coding:utf-8 -*-
import re
class Config:
    def __init__(self):
        self._config = {}
        self.readConfigFromFile()
    def getConfig(self):
        return self._config
    def readConfigFromFile(self):
        with open('./config.txt', 'r') as f:
            lines = f.readlines()
        f.close()
        config = {}
        pattern = '.*=.*'
        obj = re.compile(pattern)
        for line in lines:
            if len(obj.findall(line)) == 0:
                continue
            spl = line.split('=')
            config[spl[0]] = spl[1].replace('\n','')
        self._config = config

    def writeConfigToFile(self):
        with open('./config.txt', 'w') as f:
            for config in self._config:
                str = config+ '='+ self._config[config]+'\n'
                print(str)
                f.write(str)
            f.write('hello')
        f.close()





