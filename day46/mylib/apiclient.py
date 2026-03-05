"""A wrapper to requests"""
"""Credit to the unknown who created this wrapper for requests"""

import requests
from requests import Response
from requests.exceptions import RequestException, Timeout, HTTPError
from typing import Any


class ApiClient:
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _request(
        self,
        method: str,
        endpoint: str,
        **kwargs: Any
    ) -> Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = requests.request(
                method=method,
                url=url,
                timeout=self.timeout,
                **kwargs
            )

            # Raises HTTPError for 4xx/5xx
            response.raise_for_status()

            return response

        except Timeout as e:
            raise RuntimeError(f"Request timed out: {url}") from e

        except HTTPError as e:
            raise RuntimeError(
                f"HTTP error {e.response.status_code}: {e.response.text}"
            ) from e

        except RequestException as e:
            raise RuntimeError(f"Request failed: {str(e)}") from e

    # Only expose the common verbs
    def get(self, endpoint: str, **kwargs: Any) -> Response:
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs: Any) -> Response:
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs: Any) -> Response:
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs: Any) -> Response:
        return self._request("DELETE", endpoint, **kwargs)

# DEBUG:
if False:
    client = ApiClient("https://google.com")

    try:
        response = client.get("/", params={"active": True})
        print("EXPECT HTML: ", response.text[0:500])
    except RuntimeError as e:
        print(f"API error: {e}")

