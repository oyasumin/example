from scrapy import Item, Field

class BookItem(Item):
    name = Field()
    price = Field()

book1 = BookItem(name='Needful Things', price=45.0)
print(book1)

book2 = BookItem()
print("初始创建空对象：", book2)

book2['name'] = 'Life of Pi'
book2['price'] = 32.5
print("填充字段后，对象为：", book2)

book3 = BookItem(name='Beautiful Python', price=100.0)
print("书名：", book3['name'])
print("价格：", book3['price'])
book3['price'] = 200
print("信息修改后为：", book3)