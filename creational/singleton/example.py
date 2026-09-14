class CarSettings:
    _instance = None

    def __new__(cls):
        # __new__ chooses the object that CarSettings() returns.
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.units = "km"
            cls._instance.language= "English"
            cls._instance.brightness= 100
        return cls._instance


if __name__ == "__main__":
    dashboard_settings = CarSettings()
    mbux_settings = CarSettings()

    print("Same object:", dashboard_settings is mbux_settings)

    print("dashboard Language", dashboard_settings.language)
    print("MBUX Language", mbux_settings.language)

    print("-------------------------")

    dashboard_settings.language = "Arabic"

    print("dashboard Language", dashboard_settings.language)
    print("MBUX Language", mbux_settings.language)

    print("-------------------------")

    dashboard_settings.units = "miles"
    print("Dashboard changed the units.")
    print("MBUX units:", mbux_settings.units)
    print("Dashboard units:", dashboard_settings.units)
