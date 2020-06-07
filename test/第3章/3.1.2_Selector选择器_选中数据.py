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
selector_list = selector.xpath("//h1")
print(selector_list)

for sel in selector_list:
    print(sel.xpath('./text()'))

selector_list = selector.xpath("//h1")
print(selector_list.xpath('./text()'))

selector_list = selector.xpath('.//ul')
print(type(selector_list))
print(selector_list.css('li').xpath('./text()'))