from modules.configSIM808 import *
from modules.comunicacionGpsGprs import *
import mysql.connector
from datetime import datetime
from config import *

if __name__ == "__main__":
    sim808 = SIM808('/dev/ttyS0', 115200)
    sim808.send_command("AT")

    # Módulo GPS
    gps_data = GPSData(sim808)
    latitud, longitud = gps_data.get_location()

    db = mysql.connector.connect(
        host = IP_MV,  # Cambia esto por la IP de tu VM en Azure
        user = USER_ULISES,
        password = PASSWORD_ULISES,
        database="gps",
        port = '3306'
    )

    cursor = db.cursor()

    #INSERT
    sql = "INSERT INTO test (latitud, longitud, fecha) VALUES (%s, %s, %s)"
    val = (latitud, longitud, datetime.now())

    cursor.execute(sql, val)

    #Se confirma la transaccion
    db.commit()

    print("DEBUG: Registro(s) insertado(s):", cursor.rowcount)

    #Se cierra la conexion
    cursor.close()
    db.close()
