import scrapy

class BooksSpider(scrapy.Spider):
    # 每个爬虫的唯一标识，采用类属性
    name = "books"

    # 定义爬虫的起始点，起始点可以是多个，这里只有一个
    start_urls = ["http://books.toscrape.com/"]

    # 实现start_requests方法
    def start_requests(self):
        yield scrapy.Request("http://books.toscrape.com",
                             callback=self.parse,
                             headers={"User-Agent":"Mozilla/5.0"},
                             dont_filter=True)

    def parse(self, response):
        # 提取数据
        # 每一本书的信息在<article class="product_pod">中
        # 我们使用css()方法找到所有这样的article元素，并以此迭代
        for book in response.css("article.product_pod"):
            # 书名信息在article>h3>a元素的title属性中
            # 例如<a href="catalogue/a-light-in-the-attic_1000/index.html"
            # title="A Light in the Attic">A Light in the ...</a>
            name = book.xpath("./h3/a/@title").extract_first()
            # 书价信息在<p class="price_color">元素的文本中，
            # 如：<p class="price_color">51.77</p>
            price = book.css('p.price_color::text').extract_first()
            yield {
                "name" : name,
                "price" : price,
            }

        # 提取链接
        # 下一页的url在ul.pager>li.next>a元素中
        # 例如<li class="next"><a href="catalogue/page-2.html">next</a></li>
        next_url = response.css("ul.pager li.next a::attr(href)").extract_first()
        if next_url:
            # 如果找到下一页的url，得到绝对路径，构建新的Request对象
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)