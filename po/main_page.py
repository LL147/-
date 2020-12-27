from appium.webdriver.common.mobileby import MobileBy

from po.base_page import BasePage
from po.contact_add_page import Contact


class MainPage(BasePage):
    def goto_contact(self):
        #进入通讯录
        self.find_click(MobileBy.XPATH, "//*[@text='通讯录' and @resource-id='com.tencent.wework:id/elq']")

        return Contact(self.driver)