from constants.Api import Api as ApiConsts
from datetime import datetime
from constants.Elements import Elements
from re import findall

from entities.BaseEntities import BaseEntity, BaseEntitiesList


class Movies(BaseEntitiesList):
    """Class for store list of Movies from Api."""

    def factory(self, grouped_publications):
        """Create list of movies.

        Args:
            grouped_publications: JSON from Api with info about publications.

        Returns:
            Created structure with list of movies.

        """
        for date, movies in grouped_publications.iteritems():
            date = datetime.strptime(date, ApiConsts.SHORT_DATE)
            for movie in movies:
                self._all.append(Movie(
                    appium_driver=self._appium_driver, locator=Elements.MOVIE_ELEMENT, date=date, **movie))
        return self


class Movie(BaseEntity):
    """Class for Movie."""

    def __init__(self, appium_driver, locator, date, **kwargs):
        super(Movie, self).__init__(appium_driver, locator)
        self.date = date

        for key, value in kwargs.iteritems():
            if isinstance(value, unicode):
                if findall(string=value, pattern=r'\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d\.\d+'):
                    value = datetime.strptime(value, ApiConsts.SERVER_TIME_FORMAT)
            setattr(self, key, value)
