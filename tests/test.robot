*** Settings ***
Documentation    Suite description
Resource          ..${/}resource${/}common.robot
Suite Setup       Suite Setup
Suite Teardown    Suite Teardown
Test Setup        Test Setup
Test Teardown     Test Teardown
Test Timeout      3 minutes


*** Test Cases ***
Test title
    [Tags]    DEBUG
    Appium.Wait Until Page Contains Element        xpath=${Constants.AAAA}

    ${movieImageUrl}=   Appium.get_element_attribute
    ...                                         xpath=${Constants.AAAA}
    ...                                         attribute=app:movieImageUrl
    Log To Console     ${movieImageUrl}

*** Keywords ***
Test Setup
    [Documentation]    Preconditions for test
    [Timeout]    3 min
    Appium.Wait Until Page Contains Element   accessibility_id=${Constants.NAVIGATION_MENU_BUTTON}
    Appium.Click Element                      accessibility_id=${Constants.NAVIGATION_MENU_BUTTON}

    Appium.Wait Until Page Contains Element   class=${Constants.MAIN_MENU}
    Appium.Click Element                      xpath=${Constants.ELOKUVAT_MENU_ITEM}

Test Teardown
    [Documentation]    Teardown for test
    [Timeout]    1 min

    Comment    Test End
