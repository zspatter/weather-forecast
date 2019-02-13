# Weather-Forecast
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
