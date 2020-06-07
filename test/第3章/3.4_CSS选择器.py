from scrapy.selector import Selector
from scrapy.http import HtmlResponse

body = '''
<html>
    <head>
        <base href="http://www.example.com/" />
        <title> Example website </title>
        <style>
            .aaa{
                font-size: 20px;
                color: red;
            }
            .bbb{
                background-color: red;
            }
            .small{
                width: 100px;
            }
        </style>
    </head>
    <body>
        <div class='aaa bbb'>Hello</div>
        <div id='images-1' style='width:1230px;'>
            <a href='image1.html'>Name:Image1 <br/><img src='image1.jpg' /></a>
            <a href='image2.html'>Name:Image1 <br/><img src='image2.jpg' /></a>
            <a href='image3.html'>Name:Image1 <br/><img src='image3.jpg' /></a>
            <a href='image4.html'>Name:Image1 <br/><img src='image4.jpg' /></a>
            <a href='image5.html'>Name:Image1 <br/><img src='image5.jpg' /></a>
        </div>
        <div id='images-2' class='small'>
            <a href='image4.html'>Name:Image1 <br/><img src='image4.jpg' /></a>
            <a href='image5.html'>Name:Image1 <br/><img src='image5.jpg' /></a>
        </div>
    </body>
</html>
'''

response = HtmlResponse(url="www.example.com", body=body, encoding="utf-8")

# 选中所有的img标签节点
print(response.css('img'))
# 选中所有的base和title标签节点
print(response.css('base,title'))
# 选中div的img后代节点
print(response.css('div img'))
# 选中具有属性id且值是images-1的div节点的所有div兄弟节点
print(response.css('div[id=images-1]+div'))
# 选中body节点的直接后代节点div
print(response.css('body>div'))
# 选中包含style属性的节点
print(response.css('[style]'))
# 选中具有id属性，属性值包含连字符-，其以images开头的节点
print(response.css('[id|=images]'))
# 选中属性id值为images-1的节点
print(response.css('[id=images-1]'))
# 选中就有class属性，并且属性值包含aaa的节点
print(response.css('[class~=aaa]'))
# 选中每个div的第2个a标签节点
print(response.css('div>a:nth-child(2)'))
# 选中第二个div子节点下第一个a子节点
print(response.css('div:nth-child(2)>a:nth-child(1)'))
# 选中每个div的倒数第二个a标签节点
print(response.css('div>a:nth-last-child(2)'))
# 选取第二个div子节点下倒数第一个a子节点
print(response.css('div:nth-child(2)>a:nth-last-child(1)'))
# 选中最后一个div节点的第一个a节点
print(response.css('div:last-child>a:first-child'))
# 选择id属性值为images-1的元素
print(response.css('#images-1'))
# 选中所有a的文本
sel = response.css('a::text')
print(sel)
print(sel.extract())