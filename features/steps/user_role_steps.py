from behave import *
from lib.pages import *

@given('I have logged into qainterview as "{role}"')
def step_impl(context, role):
    context.role = role
    loginPage = AutomationLoginPage(context)
    
    loginPage.visit("http://127.0.0.1:8000/accounts/login/")
    
    loginPage.email.send_keys(role)
    """TODO: Extract from environment variables, keyfault etc"""
    loginPage.password.send_keys("password") 
    loginPage.signin_button.click()

    assert loginPage.welcome.text == "Welcome " + role

@when('I navigate to the upload page')
def step_impl(context):
    uploadPage = AutomationUploadPage(context)

    uploadPage.uploadPage.click()
    
    assert uploadPage.permission.text != 'Only members of the Admin group can upload files.'

@then('I proceed to upload a "{filetype}"')
def step_impl(context, filetype):
    uploadPage = AutomationUploadPage(context)
    loginPage = AutomationLoginPage(context)

    uploadPage.file_upload(filetype)

    assert loginPage.welcome.text == "Welcome " + context.role

    
