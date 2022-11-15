*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jarkko  jare4455
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ja  jare4455
    Output Should Contain  Username should be at least 3 letters long

Register With Valid Username And Too Short Password
    Input Credentials  jarkko  jare445
    Output Should Contain  Password should be at least 8 letters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  jarkko  jarkkoonparas
    Output Should Contain  Password should NOT only contain letters from a-z

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command