* ***Arduino UNO Card Program*** : The Arduino board coupled to the temperature so actuators will allow us first of all 
to collect the different data then send them to the central node (Raspberry Pi) and the ThingSpeak platform through 
the ESP8266 module which will ensure this server connectivity to the web.

~~~
# include <SoftwareSerial.h>    // Loading the library.

****************************** Sensors and Actuators *******************************
int ledPinR = 13;     //  Red LED 
int ledPinV = 9;       //  Green LED 
int alarme = 6;
int lm35Pin = 0;         //  Temperature sensor
String apiKey = "************";         //  Put the ThingSpeak API key
SoftwareSerial ser(10, 11);                   //  ( For RX and TX ) 

******************************** Void Setup Function ********************************
              /* This void setup () function executes the program once. */ 
void setup() {    
// Initialize the pins of the actuators as output.
pinMode(ledPinR, OUTPUT);
pinMode(ledPinV, OUTPUT);
pinMode(alarme, OUTPUT);
Serial.begin(9600);               // Enable debug serial
ser.begin(115200);             // Enable software serial
ser.println("AT+RST");      // Reinitialize ESP8266 Module
}

******************************** Void Loop Function *********************************
/* This void loop () function runs the program indefinitely as long as the object is plugged into a power source.  */ 
void loop() {
int val = 0;
val = analogRead(lm35Pin);                  // Read the sensor data
float temp = val*500.0f/1023.0f;       // Transformation of the value in degrees Celsius.

********************************* LED signaling ****************************
if(temp>30) {
// Enable the Red LED 
digitalWrite(ledPinR, HIGH);
digitalWrite(ledPinV, LOW);
}
else  {
// Enable the Green LED
digitalWrite(ledPinV, HIGH);
digitalWrite(ledPinR, LOW);
}

********************************** Alarm Activation *******************************
If (temp>70) {
// Trigger the alarm
digitalWrite(alarme, HIGH);
delay(1000);
digitalWrite(alarme, LOW);
}
Serial.println(temp);       // Show temperature.

*********************** Connection with ThingSpeak ********************************
String cm = "AT+CIPMUX=0";          // Start the TCP connection.
cm += "\r\n";
ser.println(cm);
String cmd = "AT+CIPSTART=\"TCP\",\"";     // Sending the AT command.
cmd += "api.thingspeak.com";
cmd += "\",80";
cmd += "\r\n";
ser.println(cmd); 
if(ser.find("Error")) {
Serial.println("AT+CIPSTART error");         // Displaying an error message in case of problems.
return;
}

************************** Sending data to ThingSpeak ****************************
String getStr = "GET /update?key=";       //  Prepare the GET command to ThingSpeak.
getStr += apiKey;    
getStr +="&field1=";
getStr += String(temp);
getStr += "\r\n";

// Sending the data length
cmd = "AT+CIPSEND=";
cmd += String(getStr.length());
cmd += "\r\n";
ser.println(cmd);
If (ser.find(">")) {
ser.print(getStr);
}
else{
ser.println("AT+CIPCLOSE");         // Closing the connection
}
delay(1000);

*********************** Connection with Raspberry ********************************
ser.println(cm);         // TCP connection using AT command.
String cmdd = "AT+CIPSTART=\"TCP\",\"";
cmdd += "192.168.1.86";      // Address of the Raspberry
cmdd += "\",80";
cmdd += "\r\n";
ser.println(cmdd);
if(ser.find("Error")) {
Serial.println("AT+CIPSTART error");     // Display an error message in case of problem.
return;
}

************************** Sending data to Raspberry ****************************
// Prepare the GET command to the central node
String getStrr = "GET /iot/code.php?temperature=";  
getStrr += temp;
getStrr += "\r\n";

// Sending the data length
cmdd = "AT+CIPSEND=";
cmdd += String(getStrr.length());
cmdd += "\r\n";
ser.println(cmdd);
if(ser.find(">")){
ser.print(getStrr);
}
else{
ser.println("AT+CIPCLOSE");         // Closing the connection
}

************************* Delay before re-sending data ***************************
delay(60000);     // Wait 60 seconds before the next shipment.
}   //  end of the void loop function.

~~~