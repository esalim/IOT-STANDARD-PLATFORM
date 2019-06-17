# Things.py Program
# This program recovers the data Text files then calculates the average value of the results obtained and sends it to the ThingSpeak cloud as well as to the central node. This file during its execution also makes two other programs (msg.py and dispo.py) that we will describe later.


# ************************ Loading the library  *******************************
import httplib
import urllib
import math
import time

# ************************ Définition Fonction Thermometer ****************************
def thermometer():
    with open(’data.txt’) as f:  # Opening the data file to recover the temperature
        last = None


for line in (line for line in f if line.rstrip(’\n’)):
    last = line
with open(’data2.txt’) as f:  # Opening the data2 file to recover the temperature
    last2 = None
for line in (line for line in f if line.rstrip(’\n’)):
    last2 = line

temp = (float(last) + float(last2)) / 2.0  # Average ambient temperature.
params = urllib.urlencode({’field1’: temp, ’key’:’ ** ** ** * ’})
headers = {"Content-typZZe": "application/x-www-formurlencoded", "Accept": "text/plain"}

# Creating an HTTPS connection with the ThingSpeak server
conn = httplib.HTTPSConnection("api.thingspeak.com:443")

try:
    conn.request("POST", "/update", params, headers)  # Sending the POST request
response = conn.getresponse()
print
temp
print
response.status, response.reason  # Display of answers (status & reason method)
data = response.read()
conn.close()  # Closing the connection


except:  # If there is a problem, an error message is displayed.
print("connection failed")

# **************************** Main Program ********************************
if __name__ == "__main__":
    while True:
        thermometer()  # Execution of the thermometer function.
time.sleep(3)  # Completion time.
execfile(’msg.py’)  # Execution of msg.py file.
time.sleep(3)
execfile(’dispo.py’)
time.sleep(60)  # Execution of dispo.py file.
