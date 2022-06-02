from enum import Enum
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClickType(Enum):
    DIRECT_API_CLICK = 1
    MOUSE_CLICK = 2
    JAVASCRIPT_CLICk = 3

class SelectStrategy(Enum):
    VISIBLE_TEXT=1
    VALUE=2
    INDEX=3

class ElementwaitState(Enum):
    PRESENT=1
    VISIBLE=2
    INVISIBLE=3
    CLICKABLE=4
    SELECTED=5
    FRAME_AVAILABILITY_AND_SWITCH_TO=6
    PRESENT_OF_ALL=7
    VISIBLE_OF_ALL=8
    VISIBLE_OF_ANY=9

class AlertAction(Enum):
    ACCEPT=1
    DISMISS=2

class _ElementType(Enum):
    MOBILE=1
    TABLET=2
    DESKTOP=3

class HelperFunction():

    def __init__(self, context):
        self.context = context
        self.driver_wait = WebDriverWait(self.context.driver, 30)

    def open(self, url):
        self.context.driver.get(url)

    def maximize(self):
        self.context.driver.maximize_window()    

    def close(self):
        self.context.driver.quit()

    # Helper functions that are used to identify the web locators in Selenium Python tutorial  
 
    def find_by_xpath(self, xpath):
        return self.driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
 
    def find_by_name(self, name):
        return self.driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))
 
    def find_by_id(self, id):
        return self.driver_wait.until(EC.visibility_of_element_located((By.ID, id))) 