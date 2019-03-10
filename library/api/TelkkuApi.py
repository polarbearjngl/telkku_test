import json
from entities.Movies import Movies
from library.api import Api
from constants.Api import Api as ApiConsts


class TelkkuApi(Api):

    def get_upcoming_movies(self):
        upcoming_movies = self.get(url=ApiConsts.UPCOMING_MOVIES)
        movies = json.loads(upcoming_movies.content)
        return Movies(appium_driver=self._appium_driver).factory(movies['response']['groupedPublications'])
