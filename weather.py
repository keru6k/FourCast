try:
    import requests
except Exception as L:
    print(L)


def main():

    askLocation = str(input("Choose a location: "))
    #askAPIKey = str(input("What's your API key? "))
    location = askLocation
    APIKey = 'PUT OPENWEATHER API KEY HERE' #askAPIKey 
    APIurl = "http://api.openweathermap.org/data/2.5/weather?"

    # converting kelvin to C
    def convertK(kelvin):
        celcius = kelvin - 273.15
        return celcius
        
    url = APIurl + "q=" + location + "&appid=" + APIKey
    response = requests.get(url).json()

    tkvn = response['main']['temp']
    tkvnCels = convertK(tkvn)
    weatherType = response['weather'][0]['description']


    print(f"Weather in {location}: {weatherType}")
    print(f"Temp in {location}: {int(tkvnCels)}°C")
    #if in command line like CMD that auto closes after the program is done:
    input('Please press any to exit')
    
main()
