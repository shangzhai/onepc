# -*- coding:utf-8 -*-
import re

from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

s=BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
links=s.find_all('a')
for x in links:
    print x.name,x['href'],x.get_text()

node=s.find('a',href='http://example.com/lacie')
print node.name,node['href'],node.get_text()

node=s.find('a',href=re.compile('lli'))
print node.name,node['href'],node.get_text()

node=s.find('p',class_='title')
print node.name,node['class'],node.get_text()