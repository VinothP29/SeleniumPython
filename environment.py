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
 
def after_all(context):
    pass

def before_scenario(context, scenario):
    config = ConfigParser()
    print((os.path.join(os.getcwd(), 'setup.cfg')))
    my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(my_file)
    context.driver = get_browser(config.get('Environment', 'Browser'))

def after_scenario(context, scenario):
    context.driver.close()