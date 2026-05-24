import requests
from config import BASE_URL, TOKEN


class ApiClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        }

    def post(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=data, headers=self.headers)
        return response

    def put(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=data, headers=self.headers)
        return response

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.headers)
        return response