from selenium import webdriver
from helper.helper_base import HelperFunction

class DemoCRM(HelperFunction):

    homepage_field = "txt%s"
    login = "btnLogin"

    def verify_homepage_launch(self):
        title = self.context.driver.title
        return title

    def enter_fieldvalue(self, field, value):
        self.find_by_name(self.homepage_field % field).send_keys(value)

    click_login_button = lambda self: self.find_by_id(self.login).click()

    def verify_user_login(self):
        if self.find_by_id("menu_dashboard_index"):
            return True
