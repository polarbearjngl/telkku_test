from datetime import datetime, timedelta
from monthdelta import monthdelta
from robot.libraries.BuiltIn import BuiltIn
from constants.Api import Api as ApiConsts
from library.api.TelkkuApi import TelkkuApi


class BaseSteps(object):
    """Base class for Test Steps."""
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    builtin_lib = BuiltIn()  # type: BuiltIn()

    def __init__(self):
        self.appium_lib = None
        self.telkku_api = TelkkuApi()

    def try_get_web_element(self, locator):
        """Get WebElement by given locator."""
        try:
            return self.appium_lib.get_webelement(locator=locator)
        except ValueError:
            return None

    def get_date_with_offset(self, date=None, days=0, hours=0, minutes=0, month=0, seconds=0, years=0,
                             is_null_time=True):
        """Date with offset in days, month, etc."""
        date = date if date else self.server_time
        new_sysdate = date + timedelta(hours=hours, days=days, minutes=minutes, seconds=seconds) - monthdelta(month)
        new_sysdate = new_sysdate.replace(microsecond=0, year=new_sysdate.year + years)
        return self.trunc_date(date=new_sysdate) if is_null_time else new_sysdate

    @staticmethod
    def trunc_date(date):
        """Date to format %Y-%m-%d."""
        return datetime.strptime(date.strftime(ApiConsts.SHORT_DATE), ApiConsts.SHORT_DATE)

    @property
    def server_time(self):
        """Get server time from Api."""
        time = self.telkku_api.get_server_time()
        return datetime.strptime(time, ApiConsts.SERVER_TIME_FORMAT)