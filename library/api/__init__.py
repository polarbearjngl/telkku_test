import requests
from robot.libraries.BuiltIn import BuiltIn


class Api(object):
    """Basic class for API."""
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    builtin_lib = BuiltIn()  # type: BuiltIn()
    STATUS_CODE_SUCCESS = 200

    def get(self, url, params=None, code=STATUS_CODE_SUCCESS, **kwargs):
        """Basic GET request.

        Args:
            url: URL addres for request.
            params: Request params.
            code: Expected status code.

        Returns: Response.

        """
        response = requests.get(url, params=params, **kwargs)
        self.builtin_lib.should_be_equal_as_integers(response.status_code, code,
                                                     msg='Status code not equal to expected')
        return response