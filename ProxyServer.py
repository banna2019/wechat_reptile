#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
class ProxyServer():
    def __init__(self):
        self.domain = 'http://webapi.jghttp.golangapi.com/index/index/'
    def runProxy(self):
        # 获取账号余额
        self.getBalance()
        # 添加白名单
        self.setWhiteList()
        # 提取ip
        ip = self.getIp()
        print('代理IP: ',ip)
        print('----------------')
        f = open('./config/ip.txt', 'w')
        f.write(ip)
        f.close()
        return ip
    # 获取余额接口:
    def getBalance(self):
        result = requests.get(url=self.domain+'get_my_balance?neek=3677&appkey=6e127631309d71f88d8097e9ce970c17')
        result = json.loads(result.content.decode())
        print('----------------')
        print('当前余额: ',result['data']['balance'])


    # 添加白名单接口:
    def setWhiteList(self):
        requests.get(url=self.domain + 'save_white?neek=3677&appkey=6e127631309d71f88d8097e9ce970c17&white=106.86.215.136')
    # 提取ip
    def getIp(self):
        result = requests.get(url='http://d.jghttp.golangapi.com/getip?num=1&type=1&pro=&city=0&yys=0&port=1&pack=3526&ts=0&ys=0&cs=0&lb=6&sb=/&pb=45&mr=1&regions=')
        result = result.content.decode()
        return result.strip('/')
        #
    # 删除白名单的接口:
    def delWhiteList(self):
        pass
	#webapi.jghttp.golangapi.com/index/index/del_white?neek=3677&appkey=6e127631309d71f88d8097e9ce970c17&white=您的ip
    

if __name__ == '__main__':
    proxyServer = ProxyServer()
    proxyServer.runProxy()