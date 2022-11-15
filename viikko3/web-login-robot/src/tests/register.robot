*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  jarkko
    Set Password  jarkko1234
    Set Password Confirmation  jarkko1234
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ja
    Set Password  jarkko1234
    Set Password Confirmation  jarkko1234
    Submit Register Credentials
    Register Should Fail With Message  Username should be at least 3 letters long

Register With Valid Username And Too Short Password
    Set Username  jarkko
    Set Password  jarkko1
    Set Password Confirmation  jarkko1
    Submit Register Credentials
    Register Should Fail With Message  Password should be at least 8 letters long

Register With Nonmatching Password And Password Confirmation
    Set Username  jarkko
    Set Password  jarkko1234
    Set Password Confirmation  jarkko1235
    Submit Register Credentials
    Register Should Fail With Message  Passwords should match

Login After Successful Registration
    Set Username  jarkko
    Set Password  jarkko1234
    Set Password Confirmation  jarkko1234
    Submit Register Credentials
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  jarkko
    Set Password  ja
    Set Password Confirmation  ja
    Submit Register Credentials
    Go To Login Page
    Set Username  jarkko
    Set Password  ja
    Submit Login Credentials
    Login Should Fail