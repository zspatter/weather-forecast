# Weather-Forecast
[![Python Version](https://img.shields.io/badge/python-3.4%20%7C%203.5%20%7C%203.6%20%7C%203.7-blue.svg)](https://www.python.org/getit/)
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)
<br>
[![Total alerts](https://img.shields.io/lgtm/alerts/g/zspatter/weather-forecast.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/zspatter/weather-forecast/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/zspatter/weather-forecast.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/zspatter/weather-forecast/context:python)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/09d7842eba10488d8469f5ece1076945?style=plastic)](https://www.codacy.com/app/localhost_2/weather-forecast?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=zspatter/weather-forecast&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/ed402bf00c3f3bcb1d5c/maintainability)](https://codeclimate.com/github/zspatter/weather-forecast/maintainability)

A Python script that displays the 5-day weather forecast (3 hour intervals) for a given location. This was implemented using the pyOWM API (Open Weather Map). 

Locations can be searched by city name, postal code, or coordinates. Furthermore, after searching a given location, the forecast is printed to the console. After the forecast finishes, the user is prompted to search for another location. The script doesn't terminate until the user exits. Just before terminating, the forecasts for any search locations are dumped to a .csv file.

## Requirements
#### Python
You need Python 3.4 or later to run this script. You can have multiple Python versions (2.x and 3.x) installed on the same system without issue.

In Ubuntu, Mint and Debian you can install Python 3 like this:
```
$ sudo apt-get install python3 python3-pip
```
For other Linux flavors, macOS and Windows, packages are available at <https://www.python.org/getit/>

#### PyOWM
Furthermore, you need the PyOWM wrapper library for OpenWeatherMap web APIs installed locally. This dependency can be installed through the pip installer like this:
```
$ pip install pyowm
```

## Sample Output
<p align=center>
  <img src=https://github.com/zspatter/weather-forecast/blob/master/sample_output.png alt=sample console output height=1100>
</p>

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
