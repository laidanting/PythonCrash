# coding=utf-8

import requests
import re
from lxml import etree

class requestDemo1(object):

    def getRes(self, url):
        response = requests.get(url)
        resText = etree.HTML(response.content).xpath('//h3/text()')
        return ''.join(re.findall(r'\d', resText[0]))

if __name__ == '__main__':
    text = ''
    while True:
        text = requestDemo1().getRes("http://www.heibanke.com/lesson/crawler_ex00/%s" % text)
        if text == '':
            print 'Congratulations, you found the entrance to the second pass.'
            break
        temp = text
    print 'The entry of the second pass: ' + "http://www.heibanke.com/lesson/crawler_ex00/%s" % temp
