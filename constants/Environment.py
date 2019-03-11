# -*- coding: utf-8 -*-


class Environment(object):

    # Location of Android emulator executable
    ANDROID_EMULATOR_HOME = 'C:\\Android_SDK\\emulator'

    # Location of *.apk file
    APK_LOCATION = 'C:\\Users\\Александр\\Downloads\\Telegram Desktop\\app-fast-staging.apk'  #'C:\\Users\\Александр\\PycharmProjects\\telkku_test\\app.apk'

    # Testing devices names
    API_28_DEVICE_NAME = 'Nexus_5X_API_28'
    API_25_DEVICE_NAME = 'Galaxy_Nexus_API_25'
    API_21_DEVICE_NAME = 'Nexus_S_API_21'
    TIMEZONE = 'Europe/Helsinki'

    # App id
    APPLICATION_ID = 'fi.almamedia.telkkucom.TelkkuApp'

    # Default Appium Server host, port, hub, urls
    APPIUM_HOST = '127.0.0.1'
    APPIUM_PORT = '4723'
    APPIUM_HUB = 'http://' + APPIUM_HOST + ':' + APPIUM_PORT + '/wd/hub'
    APPIUM_SESSIONS = APPIUM_HUB + '/sessions'

    # Weekdays
    WEEKDAYS = {0: u'Maanantai', 1: u'Tiistai', 2: u'Keskiviikko', 3: u'Torstai', 4: u'Perjantai', 5: u'Lauantai',
                6: u'Sunnuntai'}
