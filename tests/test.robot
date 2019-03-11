*** Settings ***
Documentation    Suite description
Resource          ..${/}resource${/}common.robot
Suite Setup       Suite Setup
Suite Teardown    Suite Teardown
Test Setup        Test Setup
Test Teardown     Test Teardown
Test Timeout      5 minutes

*** Variables ***
${ELOKUVAT}    Elokuvat

*** Test Cases ***
Count Tooday Movies Count
    [Documentation]    Test of count movies on Tooday screen
    [Tags]  Elokuvat

    ${all_movies}=      TelkkuApi.Get Upcoming Movies    appium_lib=${APPIUM}

    ${movies_by_day}=    MoviesSteps.Get Movies By Day    movies=${all_movies}
    ...                                                   appium_lib=${APPIUM}

    MoviesSteps.Check Movies Count          expected_movies=${movies_by_day}


*** Keywords ***
Test Setup
    [Documentation]    Preconditions for test
    [Timeout]    3 min
    Appium.Wait Until Page Contains Element    accessibility_id=${CONSTANTS.NAVIGATION_MENU_BUTTON}
    Appium.Click Element                       accessibility_id=${CONSTANTS.NAVIGATION_MENU_BUTTON}

    Appium.Wait Until Page Contains Element    class=${CONSTANTS.MAIN_MENU}
    Appium.Click Element                       xpath=${CONSTANTS.ELOKUVAT_MENU_ITEM}

    Appium.Wait Until Page Contains Element    id=${CONSTANTS.DATE_SELECTOR}

Test Teardown
    [Documentation]    Teardown for test
    [Timeout]    1 min

    Comment    Test End. Go to start screen.
    Appium.Wait Until Page Contains Element   accessibility_id=${CONSTANTS.NAVIGATION_MENU_BUTTON}
    Appium.Click Element                      accessibility_id=${CONSTANTS.NAVIGATION_MENU_BUTTON}

    Appium.Wait Until Page Contains Element   class=${CONSTANTS.MAIN_MENU}
    Appium.Click Element                      xpath=${CONSTANTS.TV_OHJELMAT_MENU_ITEM}