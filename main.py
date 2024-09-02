import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "yashraj.vbeyond@gmail.com"
MY_PASSWORD = "Yash@6241"

MY_LAT = 26.846695
MY_LONG = 80.946167

def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <=MY_LAT+5 and MY_LONG-5 <=iss_longitude <= MY_LONG+5:
        return True


def is_nightt():
    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LONG,
        "formatted" : 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_nightt():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: LOOK UP  \n\n The ISS is above your head"
        )












