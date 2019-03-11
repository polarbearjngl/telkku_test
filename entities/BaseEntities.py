from datetime import datetime
from re import findall

from robot.libraries.BuiltIn import BuiltIn

from constants.Api import Api as ApiConsts


class BaseEntity(object):
    """Base class for appium web element."""
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    builtin_lib = BuiltIn()  # type: BuiltIn()

    def __init__(self, appium_lib, locator, n=None, **kwargs):
        self.appium_lib = appium_lib
        self.locator = locator.format(n=n) if n else locator
        if self.appium_lib:
            self._set_web_element()

        for key, value in kwargs.iteritems():
            if isinstance(value, unicode):
                if findall(string=value, pattern=r'\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d\.\d+'):
                    value = datetime.strptime(value, ApiConsts.SERVER_TIME_FORMAT)
            setattr(self, key, value)

    def click_element(self):
        self.appium_lib.click_element(locator=self.locator)

    def get_text(self):
        return self.appium_lib.get_text(locator=self.locator)

    def get_element_attribute(self, attribute):
        return self.appium_lib.get_element_attribute(locator=self.locator, attribute=attribute)

    def _set_web_element(self):
        try:
            self.web_element = self.appium_lib.get_webelement(locator=self.locator)
        except ValueError:
            self.web_element = None


class BaseEntitiesList(object):
    """Base class for appium web elements list."""

    def __init__(self, appium_lib):
        self.appium_lib = appium_lib
        self._all = []

    def get(self, **kwargs):
        """Get elements by condition."""
        if kwargs is not None:
            return filter(lambda b: self.has_entries(b.__dict__, kwargs), self._all)

    def get_by_date(self, date, attr_name='date'):
        """Get sorted elements by given date and attribute name."""
        by_date = self.get(date=date)
        if by_date:
            return sorted(by_date, key=lambda k: k.__dict__[attr_name])
        else:
            return list()

    @staticmethod
    def has_entries(full_dict, sub_dict):
        """Method return True  if sub_dict in full_dict"""
        return all(item in full_dict.items() for item in sub_dict.items())
