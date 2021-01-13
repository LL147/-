from test_xueqiu.po.content import Content
from test_xueqiu.po.pre_page import PrePage


class Markt(PrePage):
    def search(self):
        self.basepage.load("../po/maekt.yaml")
        return Content(self.basepage)