from selenium import webdriver # pylint: disable-msg=E0611
# from selenium.webdriver.common.by import By

class Google:

    def __init__(self, context):
        pass

    def launch_google(self):
        driver = webdriver.Chrome(executable_path="C:\SeleniumPython\drivers\chromedriver\chromedriver.exe")
        driver.get(url="https://www.google.com")
