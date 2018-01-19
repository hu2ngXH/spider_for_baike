#coding=utf-8
import url_manager
import html_download
import html_outputer
import html_parser

class SpyderMain(object):
    def __init__(self):#构造器
        self.urls = url_manager.urlmanager()#构造一个管理器对象
        self.downloader = html_download.htmldownload()#构造一个下载器对象
        self.parser = html_parser.htmlparser()#构造一个解析器对象
        self.outputer = html_outputer.htmloutputer()#构造一个输出器对象
    #广度优先的爬取方式
    def craw(self,root_url):
        count =1#记录当前爬取的是第几个url
        self.urls.add_new_url(root_url)#加入新的url
        while self.urls.has_new_url():
            try:#需要加入异常处理
                new_url = self.urls.get_new_url()#获取新的url
                print "craw %d : %s" %(count,new_url)
                html_cont = self.downloader.download(new_url)#下载页面,返回下载好的数据
                #print "download is over"
                #print html_cont
                new_urls,new_data = self.parser.parse(new_url,html_cont)#解析页面得到新的url列表和数据
                #print "parse is over"
                self.urls.add_new_urls(new_urls)#将新的url列表添加进入url管理器
                #print "join in is over"
                self.outputer.collect_data(new_data)#收集数据
                #print "collect is over"
                if count == 10: #循环结束条件
                    break
                count += 1
            except:
                print "craw failed"
        self.outputer.output_html()#输出整理好的数据

if __name__=="__main__":
    root_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    obj_spyder = SpyderMain()#构造一个网络爬虫对象
    obj_spyder.craw(root_url)





