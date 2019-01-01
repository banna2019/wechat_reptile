#!/usr/bin/python3
# -*- coding: utf-8 -*-
import configparser
import random
import requests
import time
from ProxyServer import ProxyServer
from pyquery import PyQuery as pq
from selenium import webdriver
# 模拟请求user_agent
header = {}
# 设置代理
proxies = {}
class Http():
    # 设置请求头
    def setHeader(self):
        userAgent = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
            'Opera/8.0 (Windows NT 5.1; U; en)',
            'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
            'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36',
        ]
        header['User-Agent'] = random.choice(userAgent)
    # 读取代理
    def setProxyServer(self):
        with open(config['DEFAULT']['proxy_server_ip_path'], 'r') as f:
            ip = f.read()
        if config['DEFAULT']['proxy_server_type'] == '1':
            proxies = {
                'http':"http://"+ip
            }
        elif config['DEFAULT']['proxy_server_type'] == '2':
            proxies = {
                'https':ip
            }
        else:
            pass
        return proxies
    # 检测代理状态
    def checkProxyServer(self,proxies):
        try:
            requests.get('http://icanhazip.com/', proxies=proxies,timeout=8)
        except:
            # 如果代理ip异常，重新获取代理ip
            return False
        else:
            return True

    # 启动代理
    def runProxyServer(self):
        # 设置http头
        http.setHeader()
        # 设置代理
        proxies = http.setProxyServer()
        # 检测代理状态
        status = http.checkProxyServer(proxies)
        if status == True:
            print('代理检测通过')
        else:
            ProxyServer()
            self.runProxyServer()
    
class Wechat():
    # 搜索公众号,获取公众号地址
    def searchWechat(self):
        url = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query=xinhuashefabu1&ie=utf8&_sug_=n&_sug_type_=&w=01019900&sut=1096&sst0=1546364229766&lkt=0%2C0%2C0'
        result = requests.get(url, proxies=proxies,headers=header,timeout=5)
        return pq(result.content)('p[class=tit]')('a').attr('href')
    
    # 打开微信公众号
    def getWechatHtml(self,url):
        browser = webdriver.PhantomJS() 
        browser.get(url) 
        time.sleep(3) 
        # 执行js得到整个dom 
        return browser.execute_script("return document.documentElement.outerHTML")
    
    # 获取文章列表
    def getArticleList(self,html):
        doc = pq(html)
        articles = doc('div[class="weui_msg_card"]')
        print(articles)
        #articles_list = []
        #i = 1
        #for article in articles.items():
            #self.getArticleInfo(article)
            #print(u'开始整合(%d/%d)' % (i, len(articles)))
            #articles_list.append(self.parse_one_article(article))
            #i += 1
            # break
        #print(articles_list)
        #return articles_list
    def getArticleInfo(self,article):
        print(article)
        
if __name__ == '__main__':
    # 读取配置文件
    config = configparser.ConfigParser()
    # 加载配置
    config.read("./config/config.ini",encoding="utf-8")
    
    # 调用http
    http = Http()
    http.runProxyServer()
    
    # 调用微信
    wechat = Wechat()
    # 搜索公众号，获取公众号地址
    wechatUrl = wechat.searchWechat()
    html = wechat.getWechatHtml(wechatUrl)
    print(html)
    wechat.getArticleList(html)
    
    
    
    
    
    
    
    