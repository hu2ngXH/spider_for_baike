#coding=utf-8
class urlmanager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self,url):#添加新的单个url
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:#说明是个全新的url
            self.new_urls.add(url)

    def add_new_urls(self,urls):  # 收集新的url列表
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)#调用函数进行单个的添加


    def has_new_url(self):#判断是否还有url未解析
        return len(self.new_urls) != 0 #不为零返回1 为零返回0

    def get_new_url(self):#取出新的url进行解析
        new_url = self.new_urls.pop()#从列表中获取并移除
        self.old_urls.add(new_url)
        return new_url


