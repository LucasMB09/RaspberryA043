class GPSData:
    def __init__(self, sim808):
        self.sim808 = sim808

    def get_location(self):
        location = self.sim808.get_gps_location()
        if location and location['latitude'] and location['longitude']:
            print("Ubicación obtenida:", location)
            return location['latitude'], location['longitude']
        print("No se pudo obtener la ubicación")
        return None, None

