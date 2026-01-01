from gpio import *
from time import *

# Pin mapping
MOTION_1 = 2   # D0
MOTION_2 = 3   # D1

LED_1 = 0      # D2
LED_2 = 1      # D5

def main():
    # Configure pins
    pinMode(MOTION_1, INPUT)
    pinMode(MOTION_2, INPUT)

    pinMode(LED_1, OUTPUT)
    pinMode(LED_2, OUTPUT)

    # Ensure LEDs start OFF
    digitalWrite(LED_1, LOW)
    digitalWrite(LED_2, LOW)

    while True:
        # Read both motion sensors
        motion_detected = (
            digitalRead(MOTION_1) == HIGH or
            digitalRead(MOTION_2) == HIGH
        )

        # Control both LEDs together
        if motion_detected:
            digitalWrite(LED_1, HIGH)
            digitalWrite(LED_2, HIGH)
        else:
            digitalWrite(LED_1, LOW)
            digitalWrite(LED_2, LOW)

        delay(100)

main()
