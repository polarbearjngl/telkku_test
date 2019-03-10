from constants import Elements
from steps import BaseSteps


class MoviesSteps(BaseSteps):

    def get_all_movies_on_page(self, locator=Elements.MOVIE_ELEMENT, n=1):
        all_movies = []
        movie = self.try_get_web_element(locator=locator.format(n=n))
        while movie:
            all_movies.append(movie)
            n += 1
            movie = self.try_get_web_element(locator=locator.format(n=n))
        return all_movies

    def check_movies_count(self, expected_movies):
        movies_on_page = self.get_all_movies_on_page()
        self.builtin_lib.should_be_equal_as_integers(len(movies_on_page), len(expected_movies),
                                                     msg='Count of movies on page not equal to expected')