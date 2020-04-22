class Observer:
    def update(self):
        raise NotImplementedError()


class DisplayElement:
    def display(self):
        raise NotImplementedError()


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.temperature = 0.0
        self.humidity = 0.0
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self):
        self.temperature = self.weather_data.temperature
        self.humidity = self.weather_data.humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature}\u00B0F degrees and {self.humidity}% humidity")
