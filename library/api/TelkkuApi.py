import json

from library.api import Api
from constants.Api import Api as ApiConsts


class TelkkuApi(Api):

    def get_upcoming_movies(self):
        movies = self.get(url=ApiConsts.UPCOMING_MOVIES)
        return json.loads(movies.content)
