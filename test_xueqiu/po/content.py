from appium.webdriver.common.mobileby import MobileBy

from test_xueqiu.po.base_page import BasePage


class Content(BasePage):
    def content(self):
        self.find_send(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']", "aaa")

        return True