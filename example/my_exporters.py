from scrapy.exporters import BaseItemExporter
import xlwt

class ExcelItemExporter(BaseItemExporter):
    def __init__(self, file, **kwargs):
        self._configure(kwargs)
        self.file = file
        self.wbook = xlwt.Workbook()
        self.wsheet = self.wbook.add_sheet('scrapy')
        self.row = 0

    # 导出结束时被调用，可在该方法中执行某些清理工作
    def finish_exporting(self):
        self.wbook.save(self.file)

    # 负责导出爬取的每一项数据，参数item为一项爬取到的数据，每个子类必须实现该方法
    def export_item(self, item):
        # 获得item所有字段的迭代器
        fields = self._get_serialized_fields(item)
        print("fields: ", fields)
        for col, v in enumerate(x for _, x in fields):
            self.wsheet.write(self.row, col, v)
        self.row += 1