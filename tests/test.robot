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
    Appium.Wait Until Page Contains Element   accessibility_id=${Constants.NAVIGATION_MENU_BUTTON}
    Appium.Click Element                      accessibility_id=${Constants.NAVIGATION_MENU_BUTTON}

    Appium.Wait Until Page Contains Element   class=${Constants.MAIN_MENU}
    Appium.Click Element                      xpath=${Constants.ELOKUVAT_MENU_ITEM}

    Appium.Page Should Contain Element        id=${Constants.MOVIE_LIST}

*** Keywords ***
Test Setup
    [Documentation]    Preconditions for test
    [Timeout]    2 min

    Comment    Start Application
    Open Telkku Application

Test Teardown
    [Documentation]    Teardown for test
    [Timeout]    1 min

    Comment    Close Application
    Appium.Close Application
