from behave.fixture import use_fixture_by_tag
import os
from configparser import ConfigParser
from behave.fixture import use_fixture_by_tag
from helper.helper_web import get_browser
 
def before_all(context):
    config = ConfigParser()
    print((os.path.join(os.getcwd(), 'setup.cfg')))
    my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(my_file)
 
    # Reading the browser type from the configuration file for Selenium Python Tutorial
    context.driver = get_browser(config.get('Environment', 'Browser'))
 
def after_all(context):
    context.driver.close()