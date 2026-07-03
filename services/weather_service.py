import requests


class WeatherService:

    GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"

    WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


    def get_coordinates(self, city):

        response = requests.get(

            self.GEOCODE_URL,

            params={
                "name": city,
                "count": 1
            },

            timeout=10

        )

        response.raise_for_status()

        data = response.json()

        if "results" not in data:

            raise Exception(f"{city} not found.")

        location = data["results"][0]

        return {

            "city": location["name"],

            "country": location["country"],

            "latitude": location["latitude"],

            "longitude": location["longitude"],

            "timezone": location["timezone"]

        }


    def get_weather(self, city):

        location = self.get_coordinates(city)

        response = requests.get(

            self.WEATHER_URL,

            params={

                "latitude": location["latitude"],

                "longitude": location["longitude"],

                "current": [

                    "temperature_2m",

                    "relative_humidity_2m",

                    "apparent_temperature",

                    "precipitation",

                    "weather_code",

                    "wind_speed_10m",

                    "wind_direction_10m"

                ],

                "timezone": "auto"

            },

            timeout=10

        )

        response.raise_for_status()

        weather = response.json()["current"]

        return {

            "city": location["city"],

            "country": location["country"],

            "timezone": location["timezone"],

            "temperature": weather["temperature_2m"],

            "feels_like": weather["apparent_temperature"],

            "humidity": weather["relative_humidity_2m"],

            "precipitation": weather["precipitation"],

            "wind_speed": weather["wind_speed_10m"],

            "wind_direction": weather["wind_direction_10m"],

            "weather_code": weather["weather_code"]

        }