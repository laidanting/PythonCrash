#encoding=utf-8

import requests
from lxml import etree
import time

class RequestDemo(object):

    def getRes(self, url):
        response = requests.get(url)
        return response.content

    #获取用户名
    def getUserName(self, content):
        userNames = etree.HTML(content).xpath('//a[@class="u-user-name"]/text()')
        return userNames

    #获取发布的文章
    def getArticle(self, content):
        articles = etree.HTML(content).xpath('//div[@class="j-r-list-c-desc"]/a/text()')
        return articles

    #获取点赞数
    def getPraise(self, content):
        praises = etree.HTML(content).xpath('//li[@class="j-r-list-tool-l-up"]/span/text()')
        return praises

    #获取发布时间
    def getPublishTime(self, content):
        publihTime = etree.HTML(content).xpath('//span[@class="u-time  f-ib f-fr"]/text()')
        return publihTime

    # 获取文章配图
    def getArticleImg(self, content):
        publihTime = etree.HTML(content).xpath('//div[@class="j-r-list-c-img"]/a/img/@src')
        print publihTime

    #将内容保存至文件中
    def printFile(self):
        f = open("./file/budejie.txt", "w")
        page = 1
        while page <= 10:
            content = RequestDemo().getRes("http://www.budejie.com/%d" % page)
            page += 1
            userNames = RequestDemo().getUserName(content)
            articles = RequestDemo().getArticle(content)
            praises = RequestDemo().getPraise(content)
            publihTime = RequestDemo().getPublishTime(content)
            for userName, article, praise, publihTime in zip(userNames, articles, praises, publihTime):
                f.write("\n用户：{}  在{}发表了一个段子\n{} \n有{}用户喜欢这个段子\n"
                        .format(userName.encode('utf-8'), publihTime.strip(), article.strip(), praise.encode('utf-8')))
        f.close()

content = RequestDemo().getRes("http://www.budejie.com/")
time.sleep(2)
RequestDemo().getArticleImg(content)

