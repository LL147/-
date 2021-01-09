from appium.webdriver.common.mobileby import MobileBy

from test_xueqiu.po.base_page import BasePage
from test_xueqiu.po.content import Content


class Markt(BasePage):
    def search(self):
        self.find_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")
        return Content(self.driver)