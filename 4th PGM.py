#Convert the UML diagram into a python class and its methods (https://github.com/rvsp/typescript-oops/blob/master/Practice/TV-class.md)

class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.price = 0  # Add a default price if needed
        self.inches = 0  # Add a default size if needed
        self.on_off = False
        self.volume = 50

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1
        self._check_volume_bounds()

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
        self._check_volume_bounds()

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset(self):
        self.channel = 1
        self.volume = 50
        self.on_off = False

    def _check_volume_bounds(self):
        if self.volume < 0:
            self.volume = 0
        elif self.volume > 100:
            self.volume = 100

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_details(self):
        return f"Brand: {self.brand}, Screen Thickness: {self.screen_thickness} inches, " \
               f"Energy Usage: {self.energy_usage} watts, Lifespan: {self.lifespan} years, " \
               f"Refresh Rate: {self.refresh_rate} Hz"


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, viewing_angle):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.viewing_angle = viewing_angle

    def display_details(self):
        return f"Brand: {self.brand}, Screen Thickness: {self.screen_thickness} inches, " \
               f"Energy Usage: {self.energy_usage} watts, Lifespan: {self.lifespan} years, " \
               f"Viewing Angle: {self.viewing_angle} degrees"


# Example usage
led_tv = LedTV("Samsung", 0.5, 150, 10, 120)
print(led_tv.status())
led_tv.increase_volume()
led_tv.set_channel(5)
print(led_tv.status())
print(led_tv.display_details())

plasma_tv = PlasmaTV("LG", 0.7, 200, 8, 180)
print(plasma_tv.status())
plasma_tv.decrease_volume()
plasma_tv.set_channel(15)
print(plasma_tv.status())
print(plasma_tv.display_details())