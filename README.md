# IoT Standard Platform 

It is a standard IoT platform. We have objects that collect
Temperatures permanently, no unavailability is tolerated,
in addition to the cloud platform responsible for managing and analyzing
collected data and to send notifications when the
temperatures exceed certain thresholds. To increase availability,
we placed a central node less constrained allowing us to have
a hybrid architecture.

## Environmental Architecture 

The architecture of our IoT environment will be a hybrid 
architecture in order to ensure high availability of the service 
and will present itself following way:

![*Architecture Plateforme IoT*](https://github.com/AbdramCoulby/IoT-Standard-Platform/blob/master/Architecture/Images/architecture_iot.png "Architecture Plateforme IoT")

It will be composed of: 
1. ***Hardware Part*** : We'll find the following components
*  *Microcontrollers (Arduino UNO & Arduino MKR1000)*
*  *An ESP8266 WiFi module that will be associated with 
the Arduino Uno board to ensure good connectivity*
*  *Temperature sensors*
*  *A voltage regulator*
*  *Actuators*
*  *A Raspberry Pi 3 which will be our central node*

2. ***Software Part*** : We will use  
*  *Arduino IDE software for programming Arduino boards*
*  *ThingSpeak platform to collect our sensor data on the cloud and develop IoT apps*
*  *The Apache server will be used to establish communications with the HTTP protocol*
*  *You can also view the results obtained from mobile 
applications such as Blynk or ThingView*

A more detailed description of these elements above from the following documentation 
[*`Architecture Plateforme IoT`*](https://github.com/AbdramCoulby/IoT-Standard-Platform/wiki)


In order to better perform all the operations we took care to develop a *flowchart of the algorithm of our environment* 
so to be able to better describe its functionalities.

![*Organigramme de l'algorithme*](https://github.com/AbdramCoulby/IoT-Standard-Platform/blob/master/Architecture/Images/algorithme_iot.png)

## Code Section

In this section we will give and describe all the codes 
we have been able to ensure a smooth operation of the platform.

* ***Arduino UNO Card Program*** : The Arduino board coupled to the temperature so actuators will allow us first of all 
to collect the different data then send them to the central node (Raspberry Pi) and the ThingSpeak platform through 
the ESP8266 module which will ensure this server connectivity to the web.

We'll find its implementation thanks to the document [*`Arduino Uno Card Program`*](Codes/Arduino_Uno_Program.md)


* ***Arduino MKR1000 Card Program*** : This Arduino board realizes
the same function as the Arduino UNO board. In addition it should be noted that it already has a built-in Wifi module. 

We'll find its implementation thanks to the document [*`Arduino MKR1000 Card Program`*](https://github.com/AbdramCoulby/IoT-Standard-Platform/blob/master/Codes/Arduino_MKR1000_Program.md)

* ***HTTP connection program*** : This program will have the role of Achieving an HTTP connection from the arduino MKR1000 
to the ThingSpeak platform as well as the central node (Raspberry Pi).

Its implementation available from the document [*`HTTP Connection Program`*](Codes/HTPP_Connection.md)

* ***Temperature Data Program*** : The programs code.php and code.php who are responsible for receiving the data 
temperature sent by the Arduino boards and store 
them within two text files data.txt and data2.txt.

Implementation : [*`Temperature Data Program`*](https://github.com/AbdramCoulby/IoT-Standard-Platform/blob/master/Codes/Temperature_codes.md)


* ***Things.py Program*** : This program recovers the data Text files then calculates the average value of the results 
obtained and sends it to the ThingSpeak cloud as well as to the central node. 
This file during its execution also makes two other programs (msg.py and dispo.py) 
that we will describe later.

Its implementation available from the document [*`Things.Py Program`*](https://github.com/AbdramCoulby/IoT-Standard-Platform/blob/master/Codes/Things.py)


* ***Mgs.pyProgram*** : This program is used to send alert messages
through the website www.twilio.com. It uses libraries
appropriate to use the twilio API to send SMS to the manager
responsible for controlling the temperature to indicate if the temperature exceeds
the thresholds.
 
 * ***Dispo.py Program*** : The purpose of this program is to check the availability of the service. It must send SMS 
 messages to indicate if one of the Arduino boards is no longer sending data.
 
 We find their implementation thanks to the document [*`Msg_and_Dispo.py Program`*](https://github.com/AbdramCoulby/IoT-Standard-Platform/blob/master/Codes/Msg_and_Dispo.py)
 
## Contribution 
You can contribute to the project in many ways, e.g. testing functionality, sending in bug reports or creating pull requests directly via GitHub. Any help is always very welcome!
