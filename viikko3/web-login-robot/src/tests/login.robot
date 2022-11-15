*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login With Incorrect Password
    Set Username  kalle
    Set Password  kalle456
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

Login With Nonexistent Username
    Set Username  jarkko
    Set Password  kalle123
    Submit Credentials
    Login Should Fail

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Submit Credentials
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail
    Login Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open
