from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlparse
import re

html1 = open("example1.html", encoding="utf-8").read()
html2 = open("example2.html", encoding="utf-8").read()
response1 = HtmlResponse(url="http://example1.com", body=html1, encoding="utf8")
response2 = HtmlResponse(url="http://example2.com", body=html2, encoding="utf8")

# 完全提取
le = LinkExtractor()
links = le.extract_links(response1)
linkList = [link.url for link in links]
print(linkList)

# allow参数
pattern = [r"/intro/\w+\.html$", r"/examples\.html$"]
# 接收一个正则表达式或一个正则表达式列表，提取绝对url与正则表达式匹配的链接
le = LinkExtractor(allow=pattern)
links = le.extract_links(response1)
linkList = [link.url for link in links]
print(linkList)

# deny参数
# 抽取匹配列表之外的链接
# 排除正则表达式或正则表达式列表满足的url，而抽取剩余的链接
pattern = "^" + urlparse(response1.url).geturl()
print(response1.url)
print(urlparse(response1.url))
print(pattern)
le = LinkExtractor(deny=pattern)
links = le.extract_links(response1)
linkList = [link.url for link in links]
print(linkList)

# allow_domains参数
# 接收一个域名或者一个域名列表，提取到指定域的链接
domains = ['github.com', 'stackoverflow.com']
le = LinkExtractor(allow_domains=domains)
links = le.extract_links(response1)
linkList = [link.url for link in links]
print(linkList)

# deny_domains参数
# 接收一个域名或者一个域名列表，排除指定域的链接
le = LinkExtractor(deny_domains='github.com')
links = le.extract_links(response1)
linkList = [link.url for link in links]
print(linkList)

# restrict_xpaths参数
# 接收一个XPath表达式或者一个XPath表达式列表，提取XPath表达式选中区域下的链接
le = LinkExtractor(restrict_xpaths='//div[@id="top"]')
links = le.extract_links(response1)
linkList = [link.url for link in links]
print(linkList)

# restrict_css参数
# 接收一个css选择器或者一个css选择器列表，提取css选择器选中区域下的链接
le = LinkExtractor(restrict_css='div#bottom')
links = le.extract_links(response1)
linkList = [link.url for link in links]
print(linkList)

# tags参数
# 接收一个标签（字符串）或一个标签列表，提取指定标签内的链接，默认为['a','arcs']
le = LinkExtractor(tags='a')
links = le.extract_links(response1)
linkList = [link.url for link in links]
print(linkList)

# attrs参数
# 接收一个属性（字符串）或一个属性列表，提取指定属性内的链接，默认为['href']
le = LinkExtractor(tags='script', attrs='src')
links = le.extract_links(response2)
print([link.url for link in links])

# process_value参数
# 接收一个形如func(value)的回调函数
# 该回调函数用于处理提取到的每一个链接，正常情况下返回一个字符串（处理结果），想要抛弃所处理链接时返回None
def process(value):
    m = re.search("javascript:goToPage\('(.*?)'", value)
    # 如果匹配，就是提取其中的url并返回，不匹配则返回原值
    if m:
        # group(0)表示匹配整体,group(1)表示匹配第一个()内的内容
        print(m)
        value = m.group(1)
        print(value)
    return value

le = LinkExtractor(process_value=process)
links = le.extract_links(response2)
print([link.url for link in links])