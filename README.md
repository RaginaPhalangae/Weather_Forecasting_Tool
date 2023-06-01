# Weather_Forecasting_Tool

Video Link : https://drive.google.com/file/d/1R6imfBd7qWSDYBCZjigrCaTryJsgIjhI/view?usp=sharing

# Brief Summary of Project:
This project is a Python script that uses the OpenWeatherMap API to
retrieve and display weather information for a given city. The script
takes a city name as a command-line argument and makes an API
request to obtain the weather data. It then parses the JSON response to
extract relevant information such as temperature, humidity, wind
speed, weather description, sunrise time, and sunset time.
The script includes a function kelvin_to_celsius_to_fahrenheit to
convert temperature from Kelvin to Celsius and Fahrenheit. The
retrieved weather data is displayed in both Celsius and Fahrenheit
units. The API key for OpenWeatherMap is obtained from the user
through input
The script handles potential exceptions such as unsuccessful API
requests, errors in parsing the JSON response, and missing data fields.
It provides appropriate error messages in case of exceptions.
To run the script, the user needs to provide a city name as a commandline argument. If no argument is provided, a message requesting a city
name is displayed

# How to use it:

Open the command prompt (cmd) on your computer.

Navigate to the directory where you saved the
show_weather.py file using the cd command. For
example, if the file is saved on the desktop, use the
following command
 
cd C:\Users\YourUsername\Desktop

Once you are in the correct directory, you can
execute the code by running the following command:

python weather.py city_name

Replace city_name with the name of the city for
which you want to get the weather information.

Press Enter to run the command.
 
