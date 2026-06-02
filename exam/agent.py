from abc import ABC, abstractmethod
import random


# ---------------------------
# Абстрактний клас Sensor
# ---------------------------
class Sensor(ABC):
    def __init__(self, name: str, unit: str):
        self.name = name
        self.unit = unit

    @abstractmethod
    def read(self):
        pass


# ---------------------------
# Датчик температури
# ---------------------------
class TemperatureSensor(Sensor):
    def __init__(self):
        super().__init__("Temperature", "°C")

    def read(self):
        return round(random.uniform(-10, 35), 1)


# ---------------------------
# Датчик вологості
# ---------------------------
class HumiditySensor(Sensor):
    def __init__(self):
        super().__init__("Humidity", "%")

    def read(self):
        return random.randint(20, 100)


# ---------------------------
# Метеостанція
# ---------------------------
class WeatherStation:
    def __init__(self, city: str):
        self.city = city
        self.__sensors = []  # приватний атрибут

    def add_sensor(self, sensor: Sensor):
        self.__sensors.append(sensor)

    def report(self) -> dict:
        temperature = None
        humidity = None

        for sensor in self.__sensors:
            value = sensor.read()

            if isinstance(sensor, TemperatureSensor):
                temperature = value

            elif isinstance(sensor, HumiditySensor):
                humidity = value

        # Визначення погодних умов
        if humidity is not None and humidity > 80:
            condition = "Дощова погода"
        elif temperature is not None and temperature > 25:
            condition = "Сонячно"
        elif temperature is not None and temperature < 0:
            condition = "Морозно"
        else:
            condition = "Хмарно"

        return {
            "city": self.city,
            "temperature_c": temperature,
            "humidity_percent": humidity,
            "condition": condition
        }


# ---------------------------
# Інструмент (Tool)
# ---------------------------
def get_weather(city: str) -> dict:
    station = WeatherStation(city)

    station.add_sensor(TemperatureSensor())
    station.add_sensor(HumiditySensor())

    return station.report()


# ---------------------------
# AI-агент
# ---------------------------
class WeatherAgent:
    def answer(self, city: str):
        data = get_weather(city)

        recommendation = ""

        if data["condition"] == "Дощова погода":
            recommendation = "Рекомендується взяти парасолю."
        elif data["temperature_c"] < 5:
            recommendation = "Одягніть теплу куртку."
        elif data["temperature_c"] > 25:
            recommendation = "Легкий одяг буде комфортним."
        else:
            recommendation = "Підійде демісезонний одяг."

        return (
            f"Місто: {data['city']}\n"
            f"Температура: {data['temperature_c']} °C\n"
            f"Вологість: {data['humidity_percent']}%\n"
            f"Стан погоди: {data['condition']}\n"
            f"Порада: {recommendation}"
        )


# ---------------------------
# Демонстрація
# ---------------------------
agent = WeatherAgent()

print(agent.answer("Львів"))
print("-" * 40)

print(agent.answer("Київ"))
print("-" * 40)

print(agent.answer("Одеса"))
