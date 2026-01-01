from gpio import *
from time import *

# ------------------ MOTION + LED (YOUR PINS) ------------------
MOTION_1 = 0   # D0
MOTION_2 = 1   # D1
LED_1    = 2   # D2
LED_2    = 5   # D5

# ------------------ TEMPERATURE + FAN (YOUR PINS) -------------
TEMP_PIN = 0   # A0
FAN_PORT = 3   # D3 (custom cable to Fan pin 0)

# ------------------ TEMPERATURE THRESHOLDS (°C) ---------------
T_OFF  = 27.0   # fan OFF at/below this
T_LOW  = 28.0   # fan LOW at/above this
T_HIGH = 32.0   # fan HIGH at/above this

# ------------------ HELPERS -----------------------------------
def raw_to_celsius(raw):
    # Packet Tracer can return 0..255 or 0..1023 depending on device/MCU
    adc_max = 1023.0 if raw > 255 else 255.0
    return (raw / adc_max) * 200.0 - 100.0  # -100 .. +100 °C

def set_fan(state):
    # state: 0=off, 1=low, 2=high
    customWrite(FAN_PORT, str(state))

# ------------------ MAIN --------------------------------------
def main():
    # Setup motion + LEDs
    pinMode(MOTION_1, INPUT)
    pinMode(MOTION_2, INPUT)
    pinMode(LED_1, OUTPUT)
    pinMode(LED_2, OUTPUT)
    digitalWrite(LED_1, LOW)
    digitalWrite(LED_2, LOW)

    # Setup fan (custom device)
    set_fan(0)
    fan_state = 0

    while True:
        # ---- (1) Motion control: if either sensor HIGH -> both LEDs ON ----
        motion_detected = (digitalRead(MOTION_1) == HIGH) or (digitalRead(MOTION_2) == HIGH)

        if motion_detected:
            digitalWrite(LED_1, HIGH)
            digitalWrite(LED_2, HIGH)
        else:
            digitalWrite(LED_1, LOW)
            digitalWrite(LED_2, LOW)

        # ---- (2) Temperature control: OFF / LOW / HIGH with hysteresis ----
        raw = analogRead(TEMP_PIN)
        temp_c = raw_to_celsius(raw)

        if temp_c >= T_HIGH:
            new_state = 2
        elif temp_c >= T_LOW:
            new_state = 1
        elif temp_c <= T_OFF:
            new_state = 0
        else:
            new_state = fan_state  # keep current state in deadband

        if new_state != fan_state:
            set_fan(new_state)
            fan_state = new_state

        delay(200)

main()
