#encoding=utf8
import urllib
import socket

class Validate(object):

    def validate(self):

        socket.setdefaulttimeout(3)
        f = open("src/proxy")
        lines = f.readlines()
        print len(lines)
        proxys = []
        for i in range(0, len(lines)):
            ip = lines[i].strip("\n").split("\t")
            proxy_host = "http://" + ip[0] + ":" + ip[1]
            proxy_temp = {"http": proxy_host}
            proxys.append(proxy_temp)
        url = "http://ip.chinaz.com/getip.aspx"
        for proxy in proxys:
            try:
                res = urllib.urlopen(url, proxies=proxy).read()
                print proxy
            except Exception, e:
                continue