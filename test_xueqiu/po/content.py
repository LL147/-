from test_xueqiu.po.pre_page import PrePage


class Content(PrePage):
    def content(self):
        self.basepage.load("../po/content.yaml")

        return True