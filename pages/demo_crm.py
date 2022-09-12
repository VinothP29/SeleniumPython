from selenium import webdriver
from helper.helper_base import HelperFunction

class DemoCRM(HelperFunction):

    homepage_field = "txt%s"
    login = "btnLogin"
    invalid_credential = "//span[text()='Invalid credentials']"
    module_name = "//a[contains(@id,'view%sModule')]"

    def verify_homepage_launch(self):
        title = self.context.driver.title
        return title

    def enter_fieldvalue(self, field, value):
        self.find_by_name(self.homepage_field % field).send_keys(value)

    click_login_button = lambda self: self.find_by_id(self.login).click()

    def verify_user_login(self):
        if self.find_by_id("menu_dashboard_index"):
            return True
    
    def verify_invalid_credential_message(self):
        if self.find_by_xpath(self.invalid_credential):
            return True

    click_on_tab = lambda self, tab_name: self.find_by_xpath(self.module_name % tab_name).click()
