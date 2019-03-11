from constants import Elements
from steps.BaseSteps import BaseSteps


class MoviesSteps(BaseSteps):
    """Class with steps methods for movies features."""

    def get_all_movies_on_page(self, appium_lib, locator=Elements.MOVIE_ELEMENT, n=1):
        """Get all movies items on current page (Elokuvat).

        Args:
            locator: Locator for search.
            n: Index for search start.

        Returns:
            List of founded items.

        """
        self.appium_lib = appium_lib if not self.appium_lib else self.appium_lib
        all_movies = []
        movie = self.try_get_web_element(locator=locator.format(n=n))
        while movie:
            all_movies.append(movie)
            n += 1
            movie = self.try_get_web_element(locator=locator.format(n=n))
        return all_movies

    def check_movies_count(self, expected_movies, appium_lib=None):
        """Check count of movies on current page.

        Args:
            expected_movies: Movies, that expected on page.

        """
        movies_on_page = self.get_all_movies_on_page(appium_lib=appium_lib)
        self.builtin_lib.should_be_equal_as_integers(len(movies_on_page), len(expected_movies),
                                                     msg='Count of movies on page not equal to expected')

    def get_movies_by_day(self, appium_lib, movies, day=None):
        self.appium_lib = appium_lib if not self.appium_lib else self.appium_lib
        if day is None:
            date_selector = self.appium_lib.get_webelement(locator=Elements.DATE_SELECTOR)
            day = int(''.join(filter(unicode.isdigit, date_selector.text)))
        return movies.get(day=day)

    @staticmethod
    def get_movies_by_date(movies, date):
        return movies.get_by_date(date=date)
