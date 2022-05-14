from selenium import webdriver
 
def get_browser(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver
