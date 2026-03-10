#!/usr/bin/env python3
# mpu_mouse.py
from mpu6050 import mpu6050
import time

sensor = mpu6050(0x68)

print("Lettura dati MPU6050... Ctrl+C per fermare")

try:
    while True:
        accel = sensor.get_accel_data()
        gyro = sensor.get_gyro_data()

        print(f"Accel | X:{accel['x']:.2f} Y:{accel['y']:.2f} Z:{accel['z']:.2f}")
        print(f"Gyro  | X:{gyro['x']:.2f} Y:{gyro['y']:.2f} Z:{gyro['z']:.2f}")
        print("-"*50)
        time.sleep(0.2)

except KeyboardInterrupt:
    print("Programma terminato.")
