import requests

class Request:
    def make_request(self, url, request_method, params):
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
