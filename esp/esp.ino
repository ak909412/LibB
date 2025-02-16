#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char* ssid = "Phone";         // Replace with your WiFi SSID
const char* password = "1234567890"; // Replace with your WiFi Password

ESP8266WebServer server(80);

// Define LED pins for each desk
const int desk1LED = D1;  // Pin for Desk 1 LED
const int desk2LED = D2;  // Pin for Desk 2 LED
const int desk3LED = D3;  // Pin for Desk 3 LED
const int desk4LED = D4;  // Pin for Desk 4 LED
const int desk5LED = D5;  // Pin for Desk 5 LED
const int desk6LED = D6;  // Pin for Desk 6 LED

// Function to control LEDs based on the received signal
void handleSignal() {
  if (server.hasArg("signal")) {
    String signal = server.arg("signal");
    Serial.println("Received signal: " + signal);

    // Extract desk number and status from the signal
    int deskNumber = signal.substring(0, signal.length() - 1).toInt();
    int status = signal.substring(signal.length() - 1).toInt();

    // Control LEDs based on the desk number and status
    switch (deskNumber) {
      case 1:
        digitalWrite(desk1LED, status == 1 ? LOW : HIGH);
        Serial.println("Desk 1 LED status: " + String(status == 1 ? "OFF" : "ON"));
        break;
      case 2:
        digitalWrite(desk2LED, status == 1 ? LOW : HIGH);
        Serial.println("Desk 2 LED status: " + String(status == 1 ? "OFF" : "ON"));
        break;
      case 3:
        digitalWrite(desk3LED, status == 1 ? LOW : HIGH);
        Serial.println("Desk 3 LED status: " + String(status == 1 ? "OFF" : "ON"));
        break;
      case 4:
        digitalWrite(desk4LED, status == 1 ? LOW : HIGH);
        Serial.println("Desk 4 LED status: " + String(status == 1 ? "OFF" : "ON"));
        break;
      case 5:
        digitalWrite(desk5LED, status == 1 ? LOW : HIGH);
        Serial.println("Desk 5 LED status: " + String(status == 1 ? "OFF" : "ON"));
        break;
      case 6:
        digitalWrite(desk6LED, status == 1 ? LOW : HIGH);
        Serial.println("Desk 6 LED status: " + String(status == 1 ? "OFF" : "ON"));
        break;
      default:
        Serial.println("Invalid desk number");
        break;
    }
  }
  server.send(200, "text/plain", "Signal received");
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  Serial.println("Connecting to WiFi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected to WiFi");
  Serial.println("IP address: " + WiFi.localIP().toString());

  // Set LED pins as output
  pinMode(desk1LED, OUTPUT);
  pinMode(desk2LED, OUTPUT);
  pinMode(desk3LED, OUTPUT);
  pinMode(desk4LED, OUTPUT);
  pinMode(desk5LED, OUTPUT);
  pinMode(desk6LED, OUTPUT);

  // Initialize LEDs to OFF state
  digitalWrite(desk1LED, LOW);
  digitalWrite(desk2LED, LOW);
  digitalWrite(desk3LED, LOW);
  digitalWrite(desk4LED, LOW);
  digitalWrite(desk5LED, LOW);
  digitalWrite(desk6LED, LOW);

  // Start the HTTP server
  server.on("/send_signal", handleSignal);
  server.begin();
  Serial.println("Server started");
}

void loop() {
  server.handleClient();
}
