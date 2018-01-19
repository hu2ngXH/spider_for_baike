#coding=utf-8
from bs4 import BeautifulSoup
import re
import urlparse

class htmlparser(object):

    def _get_new_urls(self, page_url,soup):#获取新的连接
        new_urls=set()
        #/view/123.htm 连接格式
        links = soup.find_all('a',href = re.compile(r"/item/\.*"))#\d+代表数字
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)#按照page_url的格式拼接url为一个完整的url
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,page_url,soup):#获取新的数据
        res_data = {}
        res_data['url'] = page_url
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1> 标题格式
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")#连续find得到title
        res_data['title'] = title_node.get_text()#将文本提取出来
        #<div class="lemma-summary" label-module="lemmaSummary"> 摘要格式
        summary_node = soup.find('div',class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()  # 将文本提取出来
        return res_data


    def parse(self,page_url,html_cont):#解析 返回新的url列表和数据
        if page_url is None or html_cont is None:
            return
        #print "let's parse"
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        #print "soup is obver"
        new_urls = self._get_new_urls(page_url,soup)
        #print "get_new_urls is over"
        new_data = self._get_new_data(page_url,soup)
        #print "get_new_data is over"
        return new_urls,new_data




