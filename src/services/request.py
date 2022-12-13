import requests

class Request:
    """Class making HTTP requests"""

    def make_request(self, url, request_method, params):
        """Make a request and return data about it.

        Args:
            url (str): The URL to request
            request_method (str): Any of the valid HTTP request methods in uppercase
            params (dict): Any key-value pairs that will be sent with the request

        Returns:
            tuple: Tuple containing status code and response body
        """
        request_params = params if request_method == "GET" else None
        request_data = params if request_method != "GET" else None
        response = requests.request(
            request_method,
            url,
            params=request_params,
            data=request_data,
            timeout=10
        )
        return (response.status_code, response.text)
