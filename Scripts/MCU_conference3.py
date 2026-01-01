from gpio import *
from time import *

# Pin Assignments
LED = 0           # Digital D0
MOTION = 1        # Digital D1
SPRINKLER = 2     # Digital D2
FAN = 3           # Digital D3
FIRE_MON = 4      # Digital D4
TEMP_SENSE = 0    # Analog A0

def setup():
    pinMode(LED, OUT)
    pinMode(SPRINKLER, OUT)
    pinMode(FAN, OUT)
    pinMode(MOTION, IN)
    pinMode(FIRE_MON, IN)
    print("--- CONFERENCE ROOM SYSTEM ACTIVE ---")

def main():
    setup()
    
    while True:
        # 1. READ INPUTS
        motion_val = digitalRead(MOTION)
        fire_val = digitalRead(FIRE_MON)
        temp_val = analogRead(TEMP_SENSE) # Returns 0 to 1023
        
        # 2. LOGIC: LIGHTS & FAN (Occupancy)
        if motion_val > 0: # Using > 0 is safer than == HIGH
            digitalWrite(LED, HIGH)
            digitalWrite(FAN, HIGH)
            occ_status = "OCCUPIED"
        else:
            digitalWrite(LED, LOW)
            digitalWrite(FAN, LOW)
            occ_status = "EMPTY"

        # 3. LOGIC: SPRINKLER (Safety)
        # In PT, Fire Monitor often sends a value > 0 when smoke is present
        if fire_val > 0 or temp_val > 300: 
            digitalWrite(SPRINKLER, HIGH)
            fire_status = "!!! FIRE ALARM !!!"
        else:
            digitalWrite(SPRINKLER, LOW)
            fire_status = "SAFE"

        # 4. STATUS LOGS
        print("ROOM: " + occ_status + " | FIRE: " + fire_status)
        print("DEBUG: Motion=" + str(motion_val) + " | Fire=" + str(fire_val) + " | Temp=" + str(temp_val))
        
        delay(1500)

if __name__ == "__main__":
    main()