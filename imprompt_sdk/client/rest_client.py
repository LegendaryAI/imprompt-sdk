import requests


class APIError(Exception):
    """Custom exception for API-related errors."""
    pass


class InvalidResponseError(Exception):
    """Custom exception for invalid JSON responses."""
    pass


class TimeoutError(Exception):
    """Custom exception for request timeout."""

    def __init__(self, method, endpoint):
        self.method = method
        self.endpoint = endpoint
        super().__init__(f"Request timed out: {method} {endpoint}")


class RestClient:
    def __init__(self, base_url, timeout=30):
        self.base_url = base_url
        self.timeout = timeout

    def _request(self, method, endpoint, data=None, headers=None, params=None):
        url = self.base_url + endpoint
        try:
            response = requests.request(method, url, json=data, headers=headers,
                                        params=params, timeout=self.timeout)
            response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
            return response
        except requests.exceptions.Timeout:
            raise TimeoutError(method, endpoint)
        except requests.exceptions.RequestException as e:
            raise APIError(f"Request failed: {e}")
        except ValueError as e:
            raise InvalidResponseError(f"Invalid JSON response: {e}")
