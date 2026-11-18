import requests
import time

class ESP32Webserver:
    def __init__(self, ESP32_ip: str):
        self.ESP32_ip = ESP32_ip

    def get_data(self, path: str | None = None) -> dict:
        if path:
            data_url = f"http://{self.ESP32_ip}/{path}"
        else:
            data_url = f"http://{self.ESP32_ip}"

        try:
            response = requests.get(data_url, timeout=3)
            if response.status_code == 200:
                data = response.json()
                return(data)
            else:
                return(f"server error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            return(e)

    def send_data(self, path: str) -> None:
        pass