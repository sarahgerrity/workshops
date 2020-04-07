from hfdp.ch2_observer.weather_tracking_app.observers import CurrentConditionsDisplay
from hfdp.ch2_observer.weather_tracking_app.weather_data import WeatherData

if __name__ == '__main__':
    w_data = WeatherData()
    current_display = CurrentConditionsDisplay(w_data)

    w_data.set_measurements(80, 65, 30.4)
    w_data.set_measurements(82, 70, 29.2)
    w_data.set_measurements(78, 90, 29.2)