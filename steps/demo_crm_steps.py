from behave import given, when, then # pylint: disable-msg=E0611
from pages.demo_crm import DemoCRM # pylint: disable-msg=E0611

@given('I am in demo crm login page')
def verify_homepage(context):
    page_title = DemoCRM(context).verify_homepage_launch()
    assert page_title == "OrangeHRM"

@when('I enter the below credential in crm login page')
def enter_value(context):
    for row in context.table:
        DemoCRM(context).enter_fieldvalue(row['fieldname'], row['fieldvalue'])

@when('I click login button')
def click_login(context):
    DemoCRM(context).click_login_button()

@then('I verify user is logged in successfully')
def verify_login(context):
    logged_in = DemoCRM(context).verify_user_login()
    assert logged_in == True

@then('I verify invalid credentials alert is displayed')
def verify_invalid_credential_alert(context):
    message_displayed = DemoCRM(context).verify_invalid_credential_message()
    assert message_displayed == True