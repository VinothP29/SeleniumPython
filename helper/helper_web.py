from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
 
def get_browser(browser):
    if browser == "chrome":
        # options = Options()
        # options.headless = False
        # options.add_experimental_option("useAutomationExtension", False)
        # options.add_experimental_option("excludeSwitches",["enable-automation"]) 
        # driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        options = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=options)
        
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        return driver
