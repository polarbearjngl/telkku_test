class Api(object):

    TELKKU_API = 'http://www.telkku.com/api'
    PUBLICATIONS = '/publications'
    UPCOMING_MOVIES = TELKKU_API + PUBLICATIONS + '/upcoming-movies'

    SERVER_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f+02:00'
    SHORT_DATE = '%Y-%m-%d'
