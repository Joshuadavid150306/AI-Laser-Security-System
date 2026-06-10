from laser_detector import detect_intrusion
from ai_detector import detect_object
from alert_system import send_alert

while True:

    if detect_intrusion():

        image = "captured.jpg"

        result = detect_object(image)

        if result == "person":

            send_alert(image)

            print("Intruder Detected")
