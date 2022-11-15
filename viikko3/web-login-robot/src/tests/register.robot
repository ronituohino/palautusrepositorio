*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  jarkko
    Set Password  jarkko1234
    Set Password Confirmation  jarkko1234
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ja
    Set Password  jarkko1234
    Set Password Confirmation  jarkko1234
    Submit Credentials
    Register Should Fail With Message  Username should be at least 3 letters long

Register With Valid Username And Too Short Password
    Set Username  jarkko
    Set Password  jarkko1
    Set Password Confirmation  jarkko1
    Submit Credentials
    Register Should Fail With Message  Password should be at least 8 letters long

Register With Nonmatching Password And Password Confirmation
    Set Username  jarkko
    Set Password  jarkko1234
    Set Password Confirmation  jarkko1235
    Submit Credentials
    Register Should Fail With Message  Passwords should match


*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}
    
Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail
    Register Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}