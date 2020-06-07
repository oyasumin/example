from scrapy.http import HtmlResponse

body = '''
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

response = HtmlResponse(url="http://www.example.com", body=body, encoding="utf8")
print(response.selector)

print(response.xpath(".//h1/text()").extract())
print(response.css("li::text").extract())