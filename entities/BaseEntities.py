class BaseEntity(object):
    """Base class for appium web element."""

    def __init__(self, appium_driver, locator):
        self._appium_driver = appium_driver
        self.locator = locator
        if self._appium_driver:
            try:
                self.web_element = self._appium_driver.get_webelement(locator=self.locator)
            except ValueError:
                self.web_element = None

    def click_element(self):
        self._appium_driver.click_element(locator=self.locator)

    def get_text(self):
        return self._appium_driver.get_text(locator=self.locator)

    def get_element_attribute(self, attribute):
        return self._appium_driver.get_element_attribute(locator=self.locator, attribute=attribute)


class BaseEntitiesList(object):
    """Base class for appium web elements list."""

    def __init__(self, appium_driver):
        self._appium_driver = appium_driver
        self._all = []

    def get(self, **kwargs):
        """Get elements by condition."""
        if kwargs is not None:
            return filter(lambda b: self.has_entries(b.__dict__, kwargs), self._all)

    def get_by_date(self, date):
        by_date = self.get(date=date)
        if by_date:
            return sorted(by_date, key=lambda k: k.startTime)
        else:
            return list()

    @staticmethod
    def has_entries(full_dict, sub_dict):
        """Method return True  if sub_dict in full_dict"""
        return all(item in full_dict.items() for item in sub_dict.items())
