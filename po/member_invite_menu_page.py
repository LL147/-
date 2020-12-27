from appium.webdriver.common.mobileby import MobileBy

from po.address_list_page import AddressList
from po.base_page import BasePage


class MemberInviteMenu(BasePage):

    def add_manully(self):
        #进入手动添加信息
        self.find_click(MobileBy.XPATH, "//*[@text='手动输入添加']")

        return AddressList(self.driver)