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
        self.send_command('AT+CGNSPWR=1', wait=2)
        response = self.send_command('AT+CGNSINF', wait=2)
        for line in response:
            line = line.strip()
            if '+CGNSINF' in line:
                try:
                    data = line.split(',')
                    print("Datos GPS (split):", data)
                    latitude = data[3] 
                    longitude = data[4]
                    return {'latitude': latitude, 'longitude': longitude}
                except IndexError as e:
                    print("Error de índice al obtener coordenadas:", e)
                    return None
        return None

