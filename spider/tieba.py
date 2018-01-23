# -*- coding:utf-8 -*-

# 贴吧爬虫
import urllib
import urllib3

def loadPage(url,filename):
    """
        作用:根据url发送请求，获取服务器响应文件
        url:需要爬的url地址
        filename：处理的文件名
    """
    print("正在下载"+filename)
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    }

    # request = urllib.request(url,headers = headers)
    # request = urllib.request(url,headers = headers)
    # return urllib.urlopen(request).read()
