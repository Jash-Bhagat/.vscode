# Simulating a Smart IoT Temperature Sensor
sensor_name = "DHT22_Room_1"
raw_sensor_reading = 32.6  # Temperature in Celsius

# Your Task 1: Convert this temperature to Fahrenheit using Python math
# Formula: (Celsius * 9/5) + 32
fahrenheit_temp = (raw_sensor_reading * 9/5) + 32

# Your Task 2: Print a clean message to the terminal screen
print("Sensor ID:", sensor_name)
print("Temperature in Fahrenheit:", fahrenheit_temp)
