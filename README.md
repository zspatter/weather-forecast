# Weather-Forecast
[![Python Version](https://img.shields.io/badge/python-3.4%20%7C%203.5%20%7C%203.6%20%7C%203.7-blue.svg?style=plastic)](https://www.python.org/downloads/)
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg?style=plastic)](http://unlicense.org/)
<br>
[![Total alerts](https://img.shields.io/lgtm/alerts/g/zspatter/weather-forecast.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/zspatter/weather-forecast/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/zspatter/weather-forecast.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/zspatter/weather-forecast/context:python)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/09d7842eba10488d8469f5ece1076945?style=plastic)](https://www.codacy.com/app/localhost_2/weather-forecast?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=zspatter/weather-forecast&amp;utm_campaign=Badge_Grade)

A Python script that displays the 5-day weather forecast (3 hour intervals) for a given location. This was implemented using the pyOWM API (Open Weather Map). 

Locations can be searched by city name, postal code, or coordinates. Furthermore, after searching a given location, the forecast is printed to the console. After the forecast finishes, the user is prompted to search for another location. The script doesn't terminate until the user exits. Just before terminating, the forecasts for any search locations are dumped to a .csv file.

## What I Learned
* Python Syntax
* Familiarity with using APIs
* Data structures and data management in Python
* Command line management in Python
* File IO operations in Python

## Tasks
- [x] Add coordinates support
- [ ] Add support for other measurments such as humidity and visibility
- [ ] Add toggle for units (metric vs imperial)
