from scrapy.selector import Selector
from scrapy.http import HtmlResponse

body = '''
<html>
    <head>
        <base href="http://www.example.com/" />
        <title> Example website </title>
    </head>
    <body>
        <div id='image'>
            <a href='image1.html'>Name:Image1 <br/><img src='image1.jpg' /></a>
            <a href='image2.html'>Name:Image1 <br/><img src='image2.jpg' /></a>
            <a href='image3.html'>Name:Image1 <br/><img src='image3.jpg' /></a>
            <a href='image4.html'>Name:Image1 <br/><img src='image4.jpg' /></a>
            <a href='image5.html'>Name:Image1 <br/><img src='image5.jpg' /></a>
        </div>
    </body>
</html>
'''

response = HtmlResponse(url="www.example.com", body=body, encoding="utf-8")
print(response)

print(response.xpath('/html'))
print(response.xpath('/html/head'))

print(response.xpath('/html/body/div/a'))

print(response.xpath('//a'))

print(response.xpath("/html/body//img"))

print(response.xpath("//a/text()"))

print(response.xpath("/html/*"))

print(response.xpath("/html/body/div//*"))

print(response.xpath("//div/*/img"))

print(response.xpath("//img/@src"))

print(response.xpath("//@href"))

print(response.xpath("//a[1]/img/@*"))

sel = response.xpath("//a")[0]
print(sel)
print(sel.xpath("//img"))
print(sel.xpath(".//img"))

print(response.xpath("//img/.."))

# 选中所有a标签节点中的第三个
print(response.xpath("//a[3]"))
# 使用last函数，选中最后一个
print(response.xpath("//a[last()]"))
# 使用position函数，选中前三个
print(response.xpath("//a[position()<=3]"))

# 选中所有含有id属性的div
print(response.xpath("//div[@id]"))
# 选中所有含有id属性且值为"images"的div
print(response.xpath("//div[@id='image']"))

text = '<a href="#">Click here to go to the <strong>Next Page</strong></a>'
sel = Selector(text=text)
print(sel)

print(sel.xpath('string(/html/body/a/strong)').extract())
print(sel.xpath('/html/body/a//text()').extract())
print(sel.xpath('string(/html/body/a)').extract())

text = '''
<div>
    <p class="small info">hello world</p>
    <p class="normal info">hello scrapy</p>
</div>
'''

sel = Selector(text=text)
# 选择class属性中包含"small"的p元素
print(sel.xpath('//p[contains(@class, "small")]'))
print(sel.xpath('//p[contains(@class, "info")]'))