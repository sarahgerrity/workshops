class Subject:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()


class WeatherData(Subject):
    def __init__(self):
        super(WeatherData, self).__init__()
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temp, humid, press):
        self.temperature = temp
        self.humidity = humid
        self.pressure = press
        self.measurements_changed()
