import json
from entities.Movies import Movies
from constants.Api import Api as ApiConsts
from library.api import Api


class TelkkuApi(Api):

    def get_upcoming_movies(self, appium_lib):
        """Get upcoming movies from Api."""
        upcoming_movies = self.get(url=ApiConsts.UPCOMING_MOVIES)
        movies = json.loads(upcoming_movies.content)
        return Movies(appium_lib).factory(movies['response']['groupedPublications'])

    def get_server_time(self):
        """Get server time from Api."""
        upcoming_movies = self.get(url=ApiConsts.UPCOMING_MOVIES)
        return json.loads(upcoming_movies.content)['serverTime']
