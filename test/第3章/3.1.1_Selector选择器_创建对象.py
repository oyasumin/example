from scrapy.selector import Selector
from scrapy.http import HtmlResponse

# text = '''
# <html>
#     <body>
#         <h1>Hello World</h1>
#         <h2>Hello Scrapy</h2>
#         <b>Hello Python</b>
#         <ul>
#             <li>C++</li>
#             <li>Java</li>
#             <li>Python</li>
#         </ul>
#     </body>
# </html>
# '''
#
# selector = Selector(text=text)
# selector = Selector(text=text)
# print(selector)

body = '''
<html>
    <body>
        <h1>Hello World</h1>
        <h2>Hello Scrapy</h2>
        <b>Hello Python</b>
        <ul>
            <li>C++</li>
            <li>Java</li>
            <li>Python</li>
        </ul>
    </body>
</html>
'''

response = HtmlResponse(url='http://www.example.com', body=body, encoding="utf-8")
selector = Selector(response=response)
print(selector)