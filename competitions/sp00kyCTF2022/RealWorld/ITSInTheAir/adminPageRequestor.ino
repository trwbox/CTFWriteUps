// This is a simple program running on ESP32 to generate
// traffic to the router to be pulled from the air
#include <WiFi.h>
#include <HTTPClient.h>
#include "base64.h"

// The router is running without a password
const char* ssid = "Almond";
const char* password = "";
// base64 of admin:sp00ky{ghosts_in_the_air}
const char* auth = "Basic YWRtaW46c3AwMGt5e2dob3N0c19pbl90aGVfYWlyfQ==";
// A counter to reboot the ESP32, since according to the internet, there
// is a memory leak in the HTTPClient library, and it will eventually
// crash the ESP32 by running out of memory
unsigned long counter = 0;

void setup() {
  // Setup serial, so we can watch the logs if we
  Serial.begin(115200); 

  // Connect to the router
  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  // Wait for the connection to be established
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  // Print the IP address of the ESP32
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
 
}

void loop() {
  //Check WiFi connection status
  if(WiFi.status()== WL_CONNECTED){
    HTTPClient http;
      
    // The router domain with the admin console page
    http.begin("http://10.10.10.254/advanced/system_command.shtml");

    // Add the auth header
    http.addHeader("Authorization", auth);
    
    // Send HTTP GET request
    int httpResponseCode = http.GET();
      
    // Check the returning code
    if (httpResponseCode > 0){
       // Get the response payload
       String payload = http.getString();
       Serial.println("Request to router counter:");
       Serial.println(counter);
       Serial.println("http response code:");
       Serial.println(httpResponseCode);
       // Print the response payload if we get anything other than 200
       if(httpResponseCode != 200){
        Serial.println(payload);
       }
    } else {
       Serial.println("Error on HTTP request");
    }
    // Free resources
    http.end();
  } else {
    // If the ESP32 is not connected to the router, try to reconnect
    Serial.println("WiFi Disconnected");
  }

  // Increment the counter and reset the ESP32 if it is greater than 1200
  if(counter > 1200){
    ESP.restart();
  } else {
    counter = counter + 1;
  }
  // Wait 3 seconds before sending the next request
  delay(3000);
}
