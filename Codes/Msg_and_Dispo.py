# Mgs.pyProgram : This program is used to send alert messages through the website www.twilio.com. It uses libraries appropriate to use the twilio API to send SMS to the manager responsible for controlling the temperature to indicate if the temperature exceeds the thresholds.

# Dispo.py Program : The purpose of this program is to check the availability of the service.It must send SMS messages to indicate if one of the Arduino boards is no longer sending data.

# **********************************************************************************************************************#
# mgs.py File for twilio API
# ** ** ** ** ** ** ** ** ** ** ** ** Loading the library ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
from twilio.rest import TwilioRestClient
import time
import math

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** Parameters and actions ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
# Twilio Keys
ACCOUNT_SID = "ACc4e******310e0f48"
AUTH_TOKEN = "4d58ff********61b53a"

with open(’data.txt’) as f:  # Open the data file to retrieve the number of lines.
    last = None
for line in (line for line in f if line.rstrip(’\n’)):
    last = line
with open(’data2.txt’) as f:  # Open the data2 file to retrieve the number of lines.
    last2 = None
for line in (line for line in f if line.rstrip(’\n’)):
    last2 = line

temp = (float(last) + float(last2)) / 2.0  # Average ambient temperature.

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
if temp > 60:
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
# Creating the notification for the Twilio account
client.messages.create(
    to="+2126********",  # Phone Number
    from_="+140********",  # Twilio account number
    body="ATTENTION! HAUTE temperature detectee dans les locaux",
)
time.sleep(3)  # Completion time.

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
if math.fabs(float(last) - float(last2)) >= 50:
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
# Creating the notification for the Twilio account
client.messages.create(
    to="+2126********",  # Phone Number
    from_="+140********",  # Twilio account number
    body="ATTENTION! Problème d’intégrité sur les températures détectées",
)

# **************************************************************************************************************** #

# dispo.py File for twilio API
# ** ** ** ** ** ** ** ** ** ** ** ** Loading the library ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
from twilio.rest import TwilioRestClient
import time
import math

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** Parameters and actions ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
# Twilio Keys
ACCOUNT_SID = "ACc4e******310e0f48"
AUTH_TOKEN = "4d58ff********61b53a"

fd1 = open(’data.txt’,’r’)  # Open the data file to retrieve the number of lines.
n1 = 0
for line in fd1:
    n1 += 1

fd2 = open(’data2.txt’,’r’)  # Open the data file to retrieve the number of lines.
n2 = 0
for line in fd2:
    n2 += 1

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ***********#
fichier = open("compt.txt", "r")  # Open the file compt.txt in read mode
if str(n1) == str(fichier.read()):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
# Creation of the notification destiny the account Twilio concerning the Arduino UNO
client.messages.create(
    to="+2126********",  # Phone Number
    from_="+140********",  # Twilio account number
    body="ATTENTION! Aucune donnée transmise par l’Arduino UNO",
)

fichier_1 = open("compt.txt", "w")  # Open the file compt.txt in write mode
fichier_1.write(str(n1))
fichier_1.close()  # Closing of fichier1
fichier.close()
time.sleep(1)

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
fichier2 = open("compt2.txt", "r")
if str(n2) == str(fichier2.read()):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
# Creation of the notification destiny the account Twilio concerning the Arduino MKR1000
cclient.messages.create(
    to="+2126********",  # Phone Number
    from_="+140********",  # Twilio account number
    body="ATTENTION! Aucune donnée transmise par l’Arduino MKR1000",

    fichier_2=open("compt2.txt", "w")
fichier_2.write(str(n2))
