import requests
from datetime import datetime
import smtplib
MY_LAT = #YOUR LATITUDE
MY_LNG = #YOUR LONGITUDE
MY_EMAIL = #YOUR EMAIL
MY_PASSWORD = #YOUR PASSWORD
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG
}
def checkISS():
    response = requests.get(url ="http://api.open-notify.org/iss-now.json", params=parameters, )
    iss_lat = float(response.json()["iss_position"]["latitude"])
    iss_lng = float(response.json()["iss_position"]["longitude"])
    if (iss_lat>7 and iss_lat<17) and (iss_lng>72 and iss_lng<82):
        return True

def checkNightime():
    now = datetime.now()
    hour = now.hour
    if hour >= 18:
        return True



# checkISS()
# checkNightime()
if checkISS()and checkNightime() :
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Look above you^^\n\nThe ISS is above you right now"
    )


