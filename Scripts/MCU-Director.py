from gpio import *
from time import *

# Pin Assignments
LED_PIN = 0
FAN_PIN = 1
SPRINKLER_PIN = 2
MOTION_PIN = 3

TEMP_PIN = A0
SMOKE_PIN = A1

def setup():
    # Actuators as OUTPUT
    pinMode(LED_PIN, OUTPUT)
    pinMode(FAN_PIN, OUTPUT)
    pinMode(SPRINKLER_PIN, OUTPUT)
    
    # Sensors as INPUT
    pinMode(MOTION_PIN, INPUT)
    # Analog pins are input by default, but we declare for clarity
    pinMode(TEMP_PIN, INPUT)
    pinMode(SMOKE_PIN, INPUT)

def loop():
    while True:
        # 1. Lighting Logic (Motion Sensor)
        motion_state = digitalRead(MOTION_PIN)
        if motion_state == HIGH:
            digitalWrite(LED_PIN, HIGH)
        else:
            digitalWrite(LED_PIN, LOW)

        # 2. Climate Logic (Temp Sensor)
        # Packet Tracer analog values range from 0 to 1023
        temp_val = analogRead(TEMP_PIN)
        if temp_val > 400: # Adjust this number based on your environment
            digitalWrite(FAN_PIN, HIGH)
        else:
            digitalWrite(FAN_PIN, LOW)

        # 3. Fire Safety Logic (Smoke Sensor)
        smoke_val = analogRead(SMOKE_PIN)
        if smoke_val > 200: # If smoke is detected
            digitalWrite(SPRINKLER_PIN, HIGH)
            print("WARNING: Smoke detected! Sprinkler ON")
        else:
            digitalWrite(SPRINKLER_PIN, LOW)

        delay(1000) # Wait 1 second before next check

if __name__ == "__main__":
    setup()
    loop()