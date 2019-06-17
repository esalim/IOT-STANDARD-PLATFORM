
* ***HTTP connection program*** : 
This program will have the role of Achieving an HTTP connection from the arduino MKR1000 
to the ThingSpeak platform as well as the central node (Raspberry Pi).
~~~
Program of HTTP Connection from Arduino MKR1000 to ThingSpeak and Raspberry Pi (Central node)

************************ Loading the library. *******************************
#include <SPI.h>
#include <WiFi101.h> 

********************************** Paramètres *************************************
int ledPinB = 5;                      // Blue LED.
int ledPinJ = 6;                     // Yellow LED.
char ssid[] = "*********";                       // SSID of your WiFi.
char pass[] = "*******************";            // Your WiFi Password.
int status = WL_IDLE_STATUS;

WiFiClient  client1 , client2;   
char server[] = "api.thingspeak.com";                  // ThingSpeak Server address
char server2[] = "192.168.1.86";                          //  Raspberry server address
String writeAPIKey = "*********";                    // Key of Thingspeak.
unsigned long lastConnectionTime = 0;
const unsigned long postingInterval = 20L * 1000L; 

******************************** Void Setup Function  ********************************
              /* This void setup () function executes the program once. */ 
void setup() {    
// Initialize the pins of the actuators as output
pinMode(ledPinB, OUTPUT);
pinMode(ledPinJ, OUTPUT);
Serial.begin(9600);               // Activate debug serial

// Attempt to connect to the Wifi network
while ( status != WL_CONNECTED) {
status = WiFi.begin(ssid, pass);
delay(10000);
}

********************************  Void Loop Function *********************************
/* This void loop () function runs the program indefinitely as long as the object is plugged into a power source.  */ 
void loop() {
// Read the sensor data and convert it to Celsius degree.
int temp = analogRead(0);   
float sensorValue = temp*500.0f/1023.0f;
Serial.println(sensorValue);      // Display the data. 

****************************** LED signaling ******************************
if(sensorValue>25) {
// Enable the Yellow LED
digitalWrite(ledPinJ, HIGH);
digitalWrite(ledPinB, LOW);
}
else {
// Enable the Blue LED
digitalWrite(ledPinB, HIGH);
digitalWrite(ledPinJ, LOW);
}

******************** Connexion et envoi des données vers ThingSpeak *******************
String data = String("field1=" + String(sensorValue, DEC));    // POST command to send.
if (client1.connect(server, 443))  {                             // Connexion with the port 443.
// Display all the data.
client.println("POST /update HTTP/1.1");        
client.println("Host: api.thingspeak.com");   
client.println("Connection: close");  
client.println("User-Agent: ArduinoWiFi/1.1");
client.println("X-THINGSPEAKAPIKEY: "+writeAPIKey);
client.println("Content-Type: application/x-www-form-urlencoded");
client.print("Content-Length: ");   
client.print(data.length());   // Data Length.
client.print("\n\n");
client.print(data);
}
client.stop();         // Stop receiving data.
delay(3000);    // Wait 3s before reconnection ..

******************** Connexion et envoi des données vers La Raspberry ******************
if(client2.connect(server2, 443)) {            // Connection with the port 443.
// Display all the data.
client.println("GET /iot/code2.php?temperature="+String(sensorValue)+" HTTP/1.1");
client.println("Host: 192.168.1.86");   
client.println("Connection: close");
client.println("User-Agent: ArduinoWiFi/1.1");
client.println("Content-Type: application/x-www-form-urlencoded");
client.print("Content-Length: ");
client.print("\n\n");
}
client.stop();         // Stop receiving data.
delay(60000);    // Wait 60s before reconnection ..
}     // end of the void loop function.

~~~