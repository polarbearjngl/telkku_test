from constants.Api import Api as ApiConsts
from datetime import datetime
from constants.Elements import Elements
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
            n = 1
            date = datetime.strptime(date, ApiConsts.SHORT_DATE)
            for movie in movies:
                self._all.append(Movie(appium_lib=self.appium_lib, locator=Elements.MOVIE_ELEMENT, date=date, n=n, **movie))
                n += 1
        return self


class Movie(BaseEntity):
    """Class for Movie."""

    def __init__(self, appium_lib, locator, date, n, **kwargs):
        super(Movie, self).__init__(appium_lib, locator, n, **kwargs)
        self.date = date
        self.day = date.day
        self.month = date.month
        self.weekday = date.weekday()
        self.day_month = '%s.%s' % (self.day, self.month)
        if hasattr(self, 'imdbRating'):
            self.imdb_text = 'IMDb %s.%s' % (str(self.imdbRating)[0], str(self.imdbRating)[1])
