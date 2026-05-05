"""Example API caller using requests with Bearer token auth."""

import os

import requests
from dotenv import load_dotenv

load_dotenv()


def main() -> None:
    url = os.getenv("API_URL", "https://api.example.com/data")
    api_key = os.getenv("API_KEY", "")

    if not api_key:
        raise RuntimeError("Missing API_KEY. Add it to your .env file.")

    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers, timeout=15)

    print(f"Status: {response.status_code}")
    print("Response body:")
    print(response.text)


if __name__ == "__main__":
    main()
