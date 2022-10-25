from selenium import webdriver
from helper.helper_base import HelperFunction

class DemoCRM(HelperFunction):

    homepage_field = "%s"
    login = "//button[text()=' Login ']"
    invalid_credential = "//p[text()='Invalid credentials']"
    module_name = "//span[text()='%s']/parent::a"
    employee_information = "//h5[text()='Employee Information']"

    def verify_homepage_launch(self):
        title = self.context.driver.title
        return title

    def enter_fieldvalue(self, field, value):
        self.find_by_name(self.homepage_field % field).send_keys(value)

    click_login_button = lambda self: self.find_by_xpath(self.login).click()

    def verify_user_login(self):
        if self.find_by_xpath(self.employee_information):
            return True
    
    def verify_invalid_credential_message(self):
        if self.find_by_xpath(self.invalid_credential):
            return True

    click_on_tab = lambda self, tab_name: self.find_by_xpath(self.module_name % tab_name).click()
