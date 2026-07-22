# Simulating an Edge AI Smart Camera tracking factory safety
person_detected = True        # Boolean sensor data
wearing_safety_helmet = False # Boolean sensor data

# Task: Implement conditional logic (if/elif/else) for safety compliance
if person_detected and wearing_safety_helmet:
    print("STATUS: Access Granted. Worker is safe.")
    
elif person_detected and not wearing_safety_helmet:
    # Trigger an emergency action
    print("WARNING: Intrusion detected! Worker is NOT wearing a helmet!")
    print("Action: Triggering industrial buzzer on GPIO Pin 18.")
    
else:
    print("STATUS: Area clear. Systems normal.")
