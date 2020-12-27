from appium.webdriver.common.mobileby import MobileBy

from po.base_page import BasePage
from po.member_invite_menu_page import MemberInviteMenu


class Contact(BasePage):
    def add_connect(self):
        #添加成员
        self.swip_find(MobileBy.XPATH, "//*[@text='添加成员']").click()

        return MemberInviteMenu(self.driver)
