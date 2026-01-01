from gpio import *
from time import *

# ----------------- PINS -----------------
# Motion sensors
MOTION_DOOR_PIN   = 0   # D0
MOTION_INSIDE_PIN = 4   # D4

# LEDs
LED1_PIN = 1            # D1
LED2_PIN = 3            # D3

# Smoke + Alarm
SMOKE_PIN = 2           # A2 (analog)
ALARM_PIN = 2           # D2 (digital)

# ----------------- SETTINGS -----------------
LOOP_MS = 100
TIMEOUT_MS = 10000      # 10s for testing (use 60000 for 1 minute)

# Smoke thresholds (percent)
SMOKE_ON_PCT  = 20.0
SMOKE_OFF_PCT = 10.0

# ----------------- HELPERS -----------------
def lights_on():
    digitalWrite(LED1_PIN, HIGH)
    digitalWrite(LED2_PIN, HIGH)

def lights_off():
    digitalWrite(LED1_PIN, LOW)
    digitalWrite(LED2_PIN, LOW)

def smoke_raw_to_pct(raw):
    if raw < 0:
        raw = 0
    elif raw > 255:
        raw = 255
    return (raw / 255.0) * 100.0

# ----------------- MAIN -----------------
def main():
    # Configure pins
    pinMode(MOTION_DOOR_PIN, INPUT)
    pinMode(MOTION_INSIDE_PIN, INPUT)

    pinMode(LED1_PIN, OUTPUT)
    pinMode(LED2_PIN, OUTPUT)

    pinMode(ALARM_PIN, OUTPUT)
    digitalWrite(ALARM_PIN, LOW)

    lights_off()

    # Lighting state
    inactive_ms = TIMEOUT_MS
    prev_door = LOW

    # Alarm state
    alarm_on = False

    while True:
        # -------- (1) Smoke alarm logic --------
        smoke_raw = analogRead(SMOKE_PIN)
        smoke_pct = smoke_raw_to_pct(smoke_raw)

        if (not alarm_on) and smoke_pct >= SMOKE_ON_PCT:
            alarm_on = True
            digitalWrite(ALARM_PIN, HIGH)

        elif alarm_on and smoke_pct <= SMOKE_OFF_PCT:
            alarm_on = False
            digitalWrite(ALARM_PIN, LOW)

        # -------- (2) Lighting logic --------
        door = digitalRead(MOTION_DOOR_PIN)
        inside = digitalRead(MOTION_INSIDE_PIN)

        # Door motion → rising edge only
        if door == HIGH and prev_door == LOW:
            lights_on()
            inactive_ms = 0
        prev_door = door

        # Inside motion → resets inactivity timer
        if inside == HIGH:
            lights_on()
            inactive_ms = 0
        else:
            if inactive_ms < TIMEOUT_MS:
                inactive_ms += LOOP_MS
            if inactive_ms >= TIMEOUT_MS:
                lights_off()

        delay(LOOP_MS)

main()
