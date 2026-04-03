import os
import dotenv
import requests

dotenv.load_dotenv()

class Api:
    def __init__(self):
        self.base_url = os.getenv("BASE_API_URL")
        self.api_key = os.getenv("API_KEY")
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

    def get(self, url):
        try:
            response = requests.get(self.base_url + url, headers=self.headers, timeout=5)
            response.raise_for_status()
            data = response.json()
            return data.get("results", [])
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error {e}. Please try again.")
        except requests.exceptions.Timeout as e:
            print(f"Timeout error {e}. Please try again.")
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Something went wrong: {e}")

        return []