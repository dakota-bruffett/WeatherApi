# This is a sample Python script.
import requests
"""Fun fact the request is gonna be red alot for lab computers."""
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main ():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=paris,fr&units=imperial&appid=2235c4022250d0fe4e25df2d4020a1f0'
    data = requests.get(url).json()
    weather_description = data['weather'][0]['description']
# here is how the api is set up and how the data is set up
    temp_file= data['main']['temp']
    print(f'The weather is {weather_description}, the tempature is {temp_file:.21}F.')

"""This is how is where the tempature is being put in the data base."""

if __name__== '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
