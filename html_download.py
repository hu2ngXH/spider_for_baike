#coding=utf-8
import urllib2
class htmldownload(object):

    def download(self,url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200: #请求的状态值分别有：200请求成功、303重定向、400请求错误、401未授权、403禁止访问、404文件未找到、500服务器错误
            return None
        return response.read()#返回下载好的内容 最简单的下载方法
#这只是最简单的静态网站的爬取 以后会遇到需要登录、验证码、Ajax加载、服务器防爬虫、多线程、分布式