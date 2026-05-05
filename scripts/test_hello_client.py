"""Simple client to verify the API hello endpoint."""

import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from dotenv import load_dotenv

load_dotenv()


def main() -> None:
    url = "http://127.0.0.1:8000/api/v1/test/hello"
    api_key = os.getenv("API_KEY", "")

    if not api_key:
        raise RuntimeError("Missing API_KEY. Add it to your .env file.")

    request = Request(url=url, headers={"X-API-Key": api_key}, method="GET")
    try:
        with urlopen(request) as response:  # nosec B310 - local dev test script
            body = response.read().decode("utf-8")
            print(f"Status: {response.status}")
            print(f"Body: {body}")
    except HTTPError as exc:
        print(f"HTTP error: {exc.code} {exc.reason}")
    except URLError as exc:
        print(f"Connection error: {exc.reason}")


if __name__ == "__main__":
    main()
