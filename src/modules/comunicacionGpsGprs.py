class GPSData:
    def __init__(self, sim808):
        self.sim808 = sim808

    def get_location(self):
        location = self.sim808.get_gps_location()
        if location:
            return f"{location['latitude']}, {location['longitude']}"
        return "No se pudo obtener la ubicación"
