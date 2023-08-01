import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data. Please check your internet connection or try again later.")
        return None

def get_weather(date):
    data = get_weather_data()
    if data is not None:
        for weather in data["list"]:
            if date in weather["dt_txt"]:
                temperature = weather["main"]["temp"]
                print(f"The temperature on {date} is {temperature:.2f}°C")
                return
        print("Weather data not found for the given date.")

def get_wind_speed(date):
    data = get_weather_data()
    if data is not None:
        for weather in data["list"]:
            if date in weather["dt_txt"]:
                wind_speed = weather["wind"]["speed"]
                print(f"The wind speed on {date} is {wind_speed:.2f} m/s")
                return
        print("Wind speed data not found for the given date.")

def get_pressure(date):
    data = get_weather_data()
    if data is not None:
        for weather in data["list"]:
            if date in weather["dt_txt"]:
                pressure = weather["main"]["pressure"]
                print(f"The pressure on {date} is {pressure:.2f} hPa")
                return
        print("Pressure data not found for the given date.")

def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            date = input("Enter the date (yyyy-mm-dd HH:mm:ss): ")
            get_weather(date)
        elif choice == 2:
            date = input("Enter the date (yyyy-mm-dd HH:mm:ss): ")
            get_wind_speed(date)
        elif choice == 3:
            date = input("Enter the date (yyyy-mm-dd HH:mm:ss): ")
            get_pressure(date)
        elif choice == 0:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
