from scrapy import Item, Field

# 通过Field元数据传递额外信息
class ExampleItem(Item):
    x = Field(a='hello', b=[1,2,3])
    y = Field(a=lambda x:x**2)

e = ExampleItem(x=100, y=200)
print("-----ExampleItem实例e的Field元数据是-----")
print(type(e.fields))
print(e.fields)
field_x = e.fields['x']
print(field_x)
field_y = e.fields['y']
print(field_y)
e.fields['z'] = 123
print(e.fields)

print("\n-----ExampleItem实例e的字段值是-----")
print(e['x'])
print(e['y'])