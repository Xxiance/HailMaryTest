from fix_json import FixJson
from ESPServer import ESP32Webserver
import time

ESP_Web_server = ESP32Webserver('192.168.1.25')

database = FixJson('Database.json')

Running = True

while Running:
    esp_data = ESP_Web_server.get_data('data')
    try:
        database.add_data(esp_data)
        print(database.open_data())
        time.sleep(1)
    except Exception as E:
        print(E)


