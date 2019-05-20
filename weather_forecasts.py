import csv
from typing import Any, Dict, List, Optional, Union

import pyowm
from pyowm.weatherapi25 import Forecaster, Forecast

# creates OWM object with my unique API key
# (if forked, replace API key - keys can be generated here: https://openweathermap.org/appid)
owm = pyowm.OWM(API_key='e8105e17092b41b8c9eb198d7692a4f2', version='2.5')
forecasts: List[Dict[str, Any]] = []

# these dicts allow changes in a single location to be reflected
# across the entire program (dict keys are referenced rather than using literals)
menu_options: Dict[str, str] = {'city': '1', 'postal': '2', 'coords': '3'}
saved_data_fields: Dict[str, str] = {'loc':      'Location',
                                     'time':     'Time (UTC)',
                                     'desc':     'Description',
                                     'temp_min': 'Minimum Temperature (°C)',
                                     'temp_max': 'Maximum Temperature (°C)',
                                     'wind':     'Wind Speed (m/s)',
                                     'rain':     'Rain Accumulation (cm)',
                                     'snow':     'Snow Accumulation (cm)'}


def print_prompt() -> None:
    """
    Prints a static prompt that indicates that various menu options.
    These options correspond to a lookup method or termination.
    """
    print("Menu options:")
    print(f"\tEnter {menu_options['city']} to search by city name and country code.")
    print(f"\tEnter {menu_options['postal']} to search by postal code and country code.")
    print(f"\tEnter {menu_options['coords']} to search by coordinates.")
    print(f"\tEnter 'EXIT' to quit.")


def input_loop() -> None:
    """
    Loops that continually prints the menu prompt and accepts input
    that either indicates lookup method (city name, postal code, or
    coordinates) or exit. This function calls the corresponding lookup
    method that gathers, prints, and stores the weather data. This
    function is the basis for this CLI.

    Upon termination, this program dumps all of the gathered data for
    all queried locations to a .csv file.
    """
    while True:
        print_prompt()
        user_input: str = input("\nEnter your choice: ")

        # breaks loop if 'EXIT' is entered
        if user_input.upper() == 'EXIT':
            break
        elif user_input == menu_options['city']:
            forecaster: Optional[Forecaster] = get_forecaster_from_name()
        elif user_input == menu_options['postal']:
            forecaster: Optional[Forecaster] = get_forecaster_from_postal()
        elif user_input == menu_options['coords']:
            forecaster: Optional[Forecaster] = get_forecaster_from_coordinates()
        else:
            print('Invalid input. Try again.\n')
            continue

        # if exception thrown while creating Forecaster object,
        # forecaster will be set to None (and the loop restarts)
        if forecaster is not None:
            print_forecast(forecaster)

    dump_forecasts()


def get_forecaster_from_name() -> Optional[Forecaster]:
    """
    Queries location by city name and country code. Iff the gathered
    details correspond to a valid location, a Forecaster object
    (from PyOWM library). Otherwise, an error message is printed and
    control returns to input_loop.
    """
    city: str = input("Enter the city name: ")
    country_code: str = input("Enter the country code: ")
    lookup: str = city + ',' + country_code

    # creates Forecaster object using the location details from console
    try:
        forecaster: Optional[Forecaster] = owm.three_hours_forecast(lookup)
        return forecaster
    except pyowm.exceptions.api_response_error.NotFoundError:
        print('\nThere was an error using the parameters entered. Try again.\n')


def get_forecaster_from_postal() -> Optional[Forecaster]:
    """
    Queries location by postal code and country code. Iff the gathered
    details correspond to a valid location, a Forecaster object
    (from PyOWM library). Otherwise, an error message is printed and
    control returns to input_loop.
    """
    zip_code: str = input("Enter the postal code: ")
    country_code: str = input("Enter the country code: ")
    lookup: str = zip_code + ',' + country_code

    # creates Forecaster object using the location details from console
    try:
        forecaster: Optional[Forecaster] = owm.three_hours_forecast(lookup)
        return forecaster
    except pyowm.exceptions.api_response_error.NotFoundError:
        print('\nThere was an error using the parameters entered. Try again.\n')


def get_forecaster_from_coordinates() -> Optional[Forecaster]:
    """
    Queries location by coordinates. Iff the gathered details correspond
    to a valid location, a Forecaster object (from PyOWM library).
    Otherwise, an error message is printed and control returns to input_loop.
    """
    lat: Union[str, float] = input("Enter the latitude: ")
    long: Union[str, float] = input("Enter the longitude ")

    # verify input is a float
    if is_number(lat) and is_number(long):
        lat = float(lat)
        long = float(long)
    # otherwise, print error message and return to input_loop
    else:
        print("\nThe parameters entered are invalid. Try again.\n")
        return

    # verify input lies within lat and long ranges
    if -90 <= lat <= 90 and -180 <= long <= 180:
        # creates forecaster object using coordinates
        try:
            forecaster: Optional[Forecaster] = owm.three_hours_forecast_at_coords(lat, long)
            return forecaster
        except pyowm.exceptions.api_response_error.NotFoundError:
            print('\nThere was an error using the parameters entered. Try again.\n')
            return
    # otherwise, print error message and return to input loop
    else:
        print("\nThe parameters entered are invalid. Try again.\n")


def is_number(string: str) -> bool:
    """
    Helper function that determines if input from console is numeric.
    This is used to help determine if gathers coordinates are valid.

    :param str string: input gathered from console
    :return: bool indicating if a string can be cast to float
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


def print_forecast(forecaster: Forecaster) -> None:
    """
    Iterates through forecast for a given location printing location
    name, date/time for corresponding forecast details, a short description
    of weather at the given time, temperate range, wind speed, rainfall,
    and snowfall.

    After printing the details for a given interval, the printed values
    are added to the forecasts list as dict.

    The loop iterates through forecasts for the next 5 days at 3 hour intervals.
    :param Forecaster forecaster: generated via input from console in
        one of the get_forecaster_X() functions.
    """
    # creates forecast object from forecaster
    forecast: Forecast = forecaster.get_forecast()
    location = forecast.get_location()
    print('\n')

    for weather in forecast:
        # weather.get_rain() and weather.get_snow() return either an empty
        # dict or a dict with a single entry - gathering the length to determine
        # if the dicts are empty
        rain_length, rainfall = len(weather.get_rain()), '0'
        snow_length, snowfall = len(weather.get_snow()), '0'

        # if the length of the dict is more than 1, call the key
        # if not, rainfall is already 0 (at the beginning of for loop)
        # this gathers only the numeric value associated with the rainfall
        if rain_length > 0:
            rainfall = weather.get_rain()['3h']

        # if the length of the dict is more than 1, call the key
        # if not, snow is already 0 (at the beginning of for loop)
        # this gathers only the numeric value associated with the snowfall
        if snow_length > 0:
            snowfall = weather.get_snow()['3h']

        # prints forecast
        print(f"{location.get_name()} at "
              f"{weather.get_reference_time('iso')}"
              f"\n\tDescription:\t\t{weather.get_detailed_status()}"
              f"\n\tTemperature (°C):"
              f"\tminimum = {weather.get_temperature(unit='celsius')['temp_min']}"
              f"\tmaximum = {weather.get_temperature(unit='celsius')['temp_max']}"
              f"\n\tWind Speed (m/s):\t{weather.get_wind()['speed']}"
              f"\n\tRainfall (cm):\t\t{rainfall}"
              f"\n\tSnowfall (cm):\t\t{snowfall}\n")

        # appends forecasts list with a dict containing the values printed above
        # effectively, this creates a list of dicts with each individual dict
        # representing a specific 3 hour interval forecast
        forecasts.append({saved_data_fields['loc']:      location.get_name(),
                          saved_data_fields['time']:     weather.get_reference_time('iso'),
                          saved_data_fields['desc']:     weather.get_detailed_status(),
                          saved_data_fields['temp_min']: weather.get_temperature(unit='celsius')[
                                                             'temp_min'],
                          saved_data_fields['temp_max']: weather.get_temperature(unit='celsius')[
                                                             'temp_max'],
                          saved_data_fields['wind']:     weather.get_wind()['speed'],
                          saved_data_fields['rain']:     rainfall,
                          saved_data_fields['snow']:     snowfall})

    # separates forecast details and menu options
    print('=============================================================\n')


def dump_forecasts() -> None:
    """
    All of the data printed to the console in this session is dumped
    to forecasts.csv (each location's 5-day forecast is represented
    by 40 rows).
    """
    try:
        # opens csv file to write to
        with open('forecasts.csv', 'w') as data_dump:
            # uses established data fields for header and key search in dicts
            writer = csv.DictWriter(data_dump, fieldnames=(saved_data_fields['loc'],
                                                           saved_data_fields['time'],
                                                           saved_data_fields['desc'],
                                                           saved_data_fields['temp_min'],
                                                           saved_data_fields['temp_max'],
                                                           saved_data_fields['wind'],
                                                           saved_data_fields['rain'],
                                                           saved_data_fields['snow']))
            writer.writeheader()
            for data in forecasts:
                writer.writerow(data)
    except IOError:
        print('I/O error')


input_loop()
