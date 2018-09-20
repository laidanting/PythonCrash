#encoding=utf8
import urllib2
import urllib
import BeautifulSoup

class GetIp(object):

    def get(self):
        User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
        header = {'User-Agent': User_Agent}

        #IP代理地址，抓取页面中的IP和端口
        url = 'http://www.xicidaili.com/nn/2'
        req = urllib2.Request(url, headers=header)
        res = urllib2.urlopen(req).read()

        soup = BeautifulSoup.BeautifulSoup(res)
        ips = soup.findAll('tr')
        f = open("src/proxy", "w")
        proxys = []
        for x in range(1, len(ips)):
            ip = ips[x]
            tds = ip.findAll("td")
            ip_temp = tds[1].contents[0] + "\t" + tds[2].contents[0] + "\n"
            #proxy_host = "http://" + tds[1].contents[0] + ":" + tds[2].contents[0]
            #proxy_temp = {"http": proxy_host}
            #proxys.append(ip_temp)
            #url = "http://ip.chinaz.com/getip.aspx"
            #try:
                #res = urllib.urlopen(url, proxies=ip_temp).read()
                #print res
            #except Exception:
                #continue
            f.write(ip_temp)