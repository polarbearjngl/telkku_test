*** Settings ***
Documentation     Imports of libs, common keywords, variables
Library    AppiumLibrary    timeout=10    run_on_failure=No Operation    WITH NAME    Appium    # Sets default timeout to 10 seconds and does nothing on failure
Library    constants.Constants                                           WITH NAME    Constants
Library    robot.libraries.Process                                       WITH NAME    Process
Library    RequestsLibrary.RequestsKeywords                              WITH NAME    Requests
Library    library.api.Api                                               WITH NAME    Api


*** Variables ***
${AUTOMATION_NAME}          uiautomator2
${PLATFORM_NAME}            Android


*** Keywords ***
Suite Setup
    [Documentation]    Suite_setup
    [Timeout]    3 minute

    ${Constants}=   Get Library Instance    Constants

    Comment   Set suite variables
    Set Suite Variable    ${Constants}
    Set Suite Variable    ${APPIUM_HUB}                ${Constants.APPIUM_HUB}
    Set Suite Variable    ${APK_LOCATION}              ${Constants.APK_LOCATION}
    Set Suite Variable    ${API_28_DEVICE}             ${Constants.API_28_DEVICE_NAME}
    Set Suite Variable    ${API_25_DEVICE}             ${Constants.API_25_DEVICE_NAME}

    Comment   Android Virtual Device under test
    Set Suite Variable    ${CURRENT_TESTING_DEVICE}    ${API_25_DEVICE}

    Comment   Start Appium server
	Process.Start Process    command=appium -a ${Constants.APPIUM_HOST} -p ${Constants.APPIUM_PORT}
	...                      cwd=${Constants.ANDROID_EMULATOR_HOME}
	...                      shell=True
	...                      alias=Appium

    Wait Until Keyword Succeeds    1 min    0 sec
    ...    Api.Get    url=${Constants.APPIUM_SESSIONS}

    Comment   Start android virtual device
	Process.Start Process    command=${Constants.ANDROID_EMULATOR_HOME}${/}emulator -avd ${CURRENT_TESTING_DEVICE} -wipe-data
	...                      cwd=${Constants.ANDROID_EMULATOR_HOME}
	...                      shell=True
	...                      alias=Emulator

Suite Teardown
    [Documentation]    Suite_teardown
    [Timeout]    1 minute

    Appium.Close All Applications
    Process.Terminate All Processes


*** Keywords ***
Open Telkku Application
    [Documentation]    Open application.
    ...                *Args:*
    ...                - remote_url: URL of Appium Server Hub
    ...                - platform_name: Platform name (Android, IOS etc.)
    ...                - device_name: Name of current testing device (avd)
    ...                - app: Apk location
    ...                - automation_name: Type of appium automator
    ...                - alias: Name of created session

    [Arguments]    ${remote_url}=${APPIUM_HUB}    ${platform_name}=${PLATFORM_NAME}
    ...            ${device_name}=${CURRENT_TESTING_DEVICE}    ${app}=${APK_LOCATION}
    ...            ${automation_name}=${AUTOMATION_NAME}    ${alias}=Telkku

    Wait Until Keyword Succeeds    2 min    15 sec
    ...    Appium.Open Application    remote_url=${remote_url}
    ...                               platformName=${platform_name}
    ...                               deviceName=${device_name}
    ...                               app=${app}
    ...                               automationName=${automation_name}
    ...                               alias=${alias}