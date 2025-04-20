import serial
import time

class SIM808:
    def __init__(self, port='/dev/ttyS0', baudrate=115200, timeout=5):
        print("Inicializando módulo de configuración")
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        time.sleep(2)

    def send_command(self, command, wait=1):
        print(f"Enviando comando: {command}")
        self.ser.flushInput()
        self.ser.write((command + '\r\n').encode())
        time.sleep(wait)
        response = self.ser.readlines()
        decoded = [line.decode(errors='ignore').strip() for line in response]
        print("Respuesta recibida:", decoded)
        return decoded

    def get_gps_location(self):
        self.send_command('AT+CGNSPWR=1', wait=2)  # Encender GPS
        response = self.send_command('AT+CGNSINF', wait=2)
        for line in response:
            if '+CGNSINF' in line:
                data = line.split(',')
                return {'latitude': data[4], 'longitude': data[5]}  # Corrige si el índice es diferente
        return None
