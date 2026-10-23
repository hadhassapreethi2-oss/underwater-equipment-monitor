import random
import time

def monitor_equipment():
    print("UNDERWATER EQUIPMENT MONITORING SYSTEM")
    print("-" * 40)

    for i in range(5):
        temperature = random.randint(20, 60)
        pressure = random.randint(50, 150)
        battery = random.randint(10, 100)

        print(f"\nReading {i + 1}")
        print(f"Temperature: {temperature} C")
        print(f"Pressure: {pressure} kPa")
        print(f"Battery: {battery}%")

        if temperature > 45:
            print("ALERT: High temperature detected!")
        if pressure > 120:
            print("ALERT: High pressure detected!")
        if battery < 20:
            print("ALERT: Low battery detected!")

        if temperature <= 45 and pressure <= 120 and battery >= 20:
            print("Status: Equipment is operating normally.")

        time.sleep(1)

    print("\nMonitoring completed.")

if __name__ == "__main__":
    monitor_equipment()
