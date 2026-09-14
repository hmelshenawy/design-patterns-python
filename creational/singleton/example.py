class CarSettings:
    _instance = None

    def __new__(cls):
        # __new__ chooses the object that CarSettings() returns.
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.units = "km"
        return cls._instance


if __name__ == "__main__":
    dashboard_settings = CarSettings()
    gps_settings = CarSettings()

    print("Same object:", dashboard_settings is gps_settings)
    print("GPS units:", gps_settings.units)

    dashboard_settings.units = "miles"
    print("Dashboard changed the units.")
    print("GPS units:", gps_settings.units)
