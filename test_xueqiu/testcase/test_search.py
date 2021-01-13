from test_xueqiu.po.base_page import BasePage
from test_xueqiu.po.main import MainPage


class TestCase:
    def setup(self):
        basepage = BasePage()
        self.app = MainPage(basepage)

    def test_1(self):
        self.app.main().search().content()
