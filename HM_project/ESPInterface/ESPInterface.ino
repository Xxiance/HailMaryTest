#include <DHT.h>

#include <WiFi.h>
#include <WebServer.h>

// setup WiFi requirements
#define ssid "ZTE_2.4G_6d7Yir"
#define password "PAuPKpsA"

// sensor pins
#define DHTPIN 9
const int LDR = 8;
const int MQ135 = 10;

#define DHTTYPE DHT11 // type of DHT

DHT dht(DHTPIN, DHTTYPE); // setup DHT

WebServer server(80); // create server

// get data
void handleGetData(int LDR, int MQ135){
  int light = analogRead(LDR);
  float temp = dht.readTemperature();
  float humidity = dht.readHumidity();
  float CO2 = analogRead(MQ135);
  // turn data to dictionary
  String json_response = "{\"light\": "+ String(light) + ",\"temperature\": "+ String(temp) + ",\"humidity\": "+ String(humidity) + ",\"CO2\": "+ String(CO2) +"}";

  // send data throught JSON
  server.send(200, "application/json", json_response);
}

void setup() {
  Serial.begin(115200);

  // connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.println(".");
  }
  Serial.println("\nESP32 IP Address: " + WiFi.localIP().toString()); // print ESP32 IP

  server.on("/data", HTTP_GET, [](){
    handleGetData(LDR, MQ135);
  }); // send data when 192.x.x.x/data is called
  server.begin();

  dht.begin(); // start DHT

  // sensor pinmodes
  pinMode(LDR, INPUT);
  pinMode(MQ135, INPUT);
}

void loop() {
  server.handleClient();
}
