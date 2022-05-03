from behave import given, when # pylint: disable-msg=E0611
from pages.demo_crm import DemoCRM # pylint: disable-msg=E0611

@given('I am in demo crm login page')
def navigate_to_page(context):
    DemoCRM(context).launch_crm()

@when('I login to crm with below credential')
def login(context):
    for row in context.table:
        DemoCRM(context).login(row['fieldname'], row['fieldvalue'])
