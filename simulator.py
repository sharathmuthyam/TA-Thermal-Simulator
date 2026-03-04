import random
import time

def generate_thermal_signal(num_readings=10):
    readings = []
    temperature = 25.0  # starting temp in celsius
    
    for i in range(num_readings):
        # temperature rises gradually + small random noise
        temperature += random.uniform(20, 30)
        noise = random.uniform(-2, 2)
        reading = round(temperature + noise, 2)
        readings.append(reading)
        print(f"Reading {i+1}: {reading}°C")
    
    return readings

if __name__ == "__main__":
    print("=== Thermal Simulator Starting ===")
    signals = generate_thermal_signal()
    print(f"\nFinal readings: {signals}")
