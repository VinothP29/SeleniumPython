from behave import given # pylint: disable-msg=E0611
from pages.google import Google # pylint: disable-msg=E0611

@given('I am in google page')
def navigate_to_page(context):
    Google(context).launch_google()
