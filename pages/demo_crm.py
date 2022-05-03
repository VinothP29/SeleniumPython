import time
from selenium import webdriver
from helper.helper_base import HelperFunction

class DemoCRM(HelperFunction):

    def launch_crm(self):
        self.open(url="https://opensource-demo.orangehrmlive.com/")
        time.sleep(10)

    def login(self, field, value):
        self.find_element_by_xpath(f"//span[text()='{field}']").send_keys(value)
        if field=='Password':
            self.find_element_by_id("btnLogin").click()
        else:
            pass # Simply
