from scrapy.selector import Selector

text = '''
<html>
    <body>
        <h1>Hello World</h1>
        <h1>Hello Scrapy</h1>
        <b>Hello Python</b>
        <ul>
            <li>C++</li>
            <li>Java</li>
            <li>Python</li>
        </ul>
    </body>
</html>
'''

selector = Selector(text=text)
sl = selector.xpath('.//li')
print(sl)

print(sl[0].extract())

sl = selector.xpath(".//li/text()")
print(sl)

print(sl[1].extract())
print(sl.extract())

sl = selector.xpath(".//b")
print(sl)
print(sl.extract())
print(sl.extract_first())

text = '''
<ul>
    <li>Python 学习手册 <b>价格：99.00元</b></li>
    <li>Python 核心编程 <b>价格：88.00元</b></li>
    <li>Python 基础教程 <b>价格：80.00元</b></li>
</ul>
'''

selector = Selector(text=text)
print(selector.xpath(".//li/b/text()"))
print(selector.xpath(".//li/b/text()").extract())
print(selector.xpath(".//li/b/text()").re('\d+\.\d+'))
print(selector.xpath(".//li/b/text()").re_first('\d+\.\d+'))