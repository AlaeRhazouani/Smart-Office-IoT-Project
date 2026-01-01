from gpio import *
from time import *

# --- PIN MAPPING ROOM 1 ---
FAN1 = 0             # Digital D0
LED1 = 1             # Digital D1
MOTION1 = 2          # Digital D2
TEMP1 = 0            # Analog A0

# --- PIN MAPPING ROOM 2 ---
LED2 = 3             # Digital D3
FAN2 = 4             # Digital D4
MOTION2 = 5          # Digital D5
TEMP2 = 1            # Analog A1

# --- SETTINGS ---
TEMP_THRESHOLD = 300 # Logical threshold (~30C) to trigger fans

def setup():
    # Setup Room 1
    pinMode(FAN1, OUT)
    pinMode(LED1, OUT)
    pinMode(MOTION1, IN)
    
    # Setup Room 2
    pinMode(LED2, OUT)
    pinMode(FAN2, OUT)
    pinMode(MOTION2, IN)
    
    print("--- MINIBREAK AREA SYSTEM: ACTIVE ---")

def main():
    setup()
    
    while True:
        # 1. READ ALL SENSORS
        m1 = digitalRead(MOTION1)
        m2 = digitalRead(MOTION2)
        t1 = analogRead(TEMP1)
        t2 = analogRead(TEMP2)
        
        # 2. LOGIC ROOM 1
        # LED: Only on Motion
        # FAN: On if Motion OR Temperature is high
        if m1 == HIGH:
            digitalWrite(LED1, HIGH)
            digitalWrite(FAN1, HIGH)
            r1_msg = "Occupied"
        elif t1 > TEMP_THRESHOLD:
            digitalWrite(LED1, LOW)
            digitalWrite(FAN1, HIGH)
            r1_msg = "Overheating (Fan On)"
        else:
            digitalWrite(LED1, LOW)
            digitalWrite(FAN1, LOW)
            r1_msg = "Empty/Safe"

        # 3. LOGIC ROOM 2
        if m2 == HIGH:
            digitalWrite(LED2, HIGH)
            digitalWrite(FAN2, HIGH)
            r2_msg = "Occupied"
        elif t2 > TEMP_THRESHOLD:
            digitalWrite(LED2, LOW)
            digitalWrite(FAN2, HIGH)
            r2_msg = "Overheating (Fan On)"
        else:
            digitalWrite(LED2, LOW)
            digitalWrite(FAN2, LOW)
            r2_msg = "Empty/Safe"

        # 4. STATUS LOGS (Check the MCU Console)
        print("------------------------------------------")
        print("ROOM 1 | Status: {:18} | Temp: {}".format(r1_msg, t1))
        print("ROOM 2 | Status: {:18} | Temp: {}".format(r2_msg, t2))
        
        delay(1500)

if __name__ == "__main__":
    main()