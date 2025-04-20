import serial
import time

class SIM808:
    def __init__(self, port='/dev/ttyS0', baudrate=115200, timeout=5):
        print("Inicializando módulo de configuración")
        self.ser = serial.Serial(port, baudrate, timeout=timeout)

    def send_command(self, command, wait=1):
        """Envía un comando AT al módulo y espera la respuesta"""
        print("Comando recibido:" + command)
        self.ser.write((command + '\r\n').encode())
        time.sleep(wait)
        response = self.ser.readlines()
        print(self.ser.readlines())
        return response

    def get_gps_location(self):
        """Obtiene la ubicación GPS actual"""
        self.send_command('AT+CGNSPWR=1')  # Encender GPS
        time.sleep(2)
        response = self.send_command('AT+CGNSINF')  # Obtener datos GPS
        for line in response:
            if line.startswith(b'+CGNSINF:'):
                data = line.decode().split(',')
                return {'latitude': data[3], 'longitude': data[4]}
        return None