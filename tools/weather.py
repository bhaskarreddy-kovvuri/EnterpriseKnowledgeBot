from services.weather_service import WeatherService


class WeatherTool:

    def __init__(self):

        self.service = WeatherService()


    def execute(self, city):

        return self.service.get_weather(city)