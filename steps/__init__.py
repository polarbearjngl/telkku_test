from datetime import datetime, timedelta
import pytz
from monthdelta import monthdelta
from robot.libraries.BuiltIn import BuiltIn

from constants import Environment
from constants.Api import Api as ApiConsts


class BaseSteps(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    builtin_lib = BuiltIn()  # type: BuiltIn()

    def __init__(self, appium_driver):
        self._appium_driver = appium_driver

    def try_get_web_element(self, locator):
        try:
            return self._appium_driver.get_webelement(locator=locator)
        except ValueError:
            return None

    def get_date_with_offset(self, date=None, days=0, hours=0, minutes=0, month=0, seconds=0, years=0,
                             is_null_time=True):
        date = date if date else datetime.now(tz=pytz.timezone(Environment.TIMEZONE))
        new_sysdate = date + timedelta(hours=hours, days=days, minutes=minutes, seconds=seconds) - monthdelta(month)
        new_sysdate = new_sysdate.replace(microsecond=0, year=new_sysdate.year + years)
        return self.trunc_date(date=new_sysdate) if is_null_time else new_sysdate

    @staticmethod
    def trunc_date(date):
        return datetime.strptime(date.strftime(ApiConsts.SHORT_DATE), ApiConsts.SHORT_DATE)
