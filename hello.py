# -*- coding:utf-8 -*-
import cookielib
import urllib2

url="http://baike.baidu.com/item/Python"

rp1=urllib2.urlopen(url)

print rp1.getcode()
print len(rp1.read())


rq=urllib2.Request(url)
rq.add_header("user-agent","Mozilla/5.0")
rp2=urllib2.urlopen(rq)
print rp2.getcode()
print len(rp2.read())



cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
rp3=urllib2.urlopen(url)
t=rp3.read()
print rp3.getcode()
print len(t)
print cj
print t





