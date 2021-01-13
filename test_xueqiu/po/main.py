from test_xueqiu.po.maekt import Markt
from test_xueqiu.po.pre_page import PrePage


class MainPage(PrePage):
    def main(self):
        self.basepage.load("../po/main.yaml")

        return Markt(self.basepage)

