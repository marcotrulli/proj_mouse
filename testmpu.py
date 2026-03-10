# mpu6050_read.py
# Lettura dati da MPU6050 su Raspberry Pi via I2C

import time
import board
import busio
import adafruit_mpu6050

# Inizializza I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Crea istanza MPU6050
mpu = adafruit_mpu6050.MPU6050(i2c)

print("Inizio lettura dati MPU6050... Premi Ctrl+C per fermare.")

try:
    while True:
        # Leggi accelerazione in m/s^2
        accel = mpu.acceleration
        # Leggi giroscopio in gradi/s
        gyro = mpu.gyro

        print(f"Accelerazione X:{accel[0]:.2f} Y:{accel[1]:.2f} Z:{accel[2]:.2f} m/s²")
        print(f"Giroscopio    X:{gyro[0]:.2f} Y:{gyro[1]:.2f} Z:{gyro[2]:.2f} °/s")
        print("-" * 40)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Lettura terminata.")
