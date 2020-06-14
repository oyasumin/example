import scrapy
from ..items import BookItem
from scrapy.linkextractors import LinkExtractor

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

    # def parse(self, response):
    #     # 提取数据
    #     # 每一本书的信息在<article class="product_pod">中
    #     # 我们使用css()方法找到所有这样的article元素，并以此迭代
    #     for book in response.css("article.product_pod"):
    #         # 书名信息在article>h3>a元素的title属性中
    #         # 例如<a href="catalogue/a-light-in-the-attic_1000/index.html"
    #         # title="A Light in the Attic">A Light in the ...</a>
    #         name = book.xpath("./h3/a/@title").extract_first()
    #         # 书价信息在<p class="price_color">元素的文本中，
    #         # 如：<p class="price_color">51.77</p>
    #         price = book.css('p.price_color::text').extract_first()
    #         yield {
    #             "name" : name,
    #             "price" : price,
    #         }
    #
    #     # 提取链接
    #     # 下一页的url在ul.pager>li.next>a元素中
    #     # 例如<li class="next"><a href="catalogue/page-2.html">next</a></li>
    #     next_url = response.css("ul.pager li.next a::attr(href)").extract_first()
    #     if next_url:
    #         # 如果找到下一页的url，得到绝对路径，构建新的Request对象
    #         next_url = response.urljoin(next_url)
    #         yield scrapy.Request(next_url, callback=self.parse)

    def parse(self, response):
        # 提取数据
        # 每一本书的信息在<article class="product_pod">中
        # 我们使用css()方法找到所有这样的article元素，并以此迭代
        for sel in response.css("article.product_pod"):
            book = BookItem()
            # 书名信息在article>h3>a元素的title属性中
            # 例如<a href="catalogue/a-light-in-the-attic_1000/index.html"
            # title="A Light in the Attic">A Light in the ...</a>
            book['name'] = sel.xpath("./h3/a/@title").extract_first()
            # 书价信息在<p class="price_color">元素的文本中，
            # 如：<p class="price_color">51.77</p>
            book['price'] = sel.css('p.price_color::text').extract_first()
            yield book

        # # 提取链接
        # # 下一页的url在ul.pager>li.next>a元素中
        # # 例如<li class="next"><a href="catalogue/page-2.html">next</a></li>
        # next_url = response.css("ul.pager li.next a::attr(href)").extract_first()
        # if next_url:
        #     # 如果找到下一页的url，得到绝对路径，构建新的Request对象
        #     next_url = response.urljoin(next_url)
        #     yield scrapy.Request(next_url, callback=self.parse)

        # 传递给restrict_css参数一个CSS选择器表达式
        # 描述出下一个页链接所在的区域（在li.next下）
        le = LinkExtractor(restrict_css='ul.pager li.next')
        # 传入一个Response对象，该方法根据创建对象时所描述的提取规则
        # 在Response对象所包含的页面中提取链接，最终返回一个列表
        # 其中每个元素都是一个Link对象，即提取到的一个链接
        links = le.extract_links(response)
        if links:
            # 由于页面中的下一页链接只有一个，因此用link[0]获取Link对象
            # Link对象的url属性便是链接页面的绝对url地址（无需再调用response.urljoin方法）
            # 用其构造Request对象并提交
            next_url = links[0].url
            yield scrapy.Request(next_url, callback=self.parse)
