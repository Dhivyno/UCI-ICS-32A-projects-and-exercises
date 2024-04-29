# project3.py
#
# ICS 32A Fall 2023


import json
import urllib.parse
import urllib.request
from pathlib import Path

# All of the urls provided by the NWS API have URLs that
# begin like this; it's simply a matter of adding the rest of the URL
# and its query parameters to the end of this.
BASE_NWS_URL = 'https://api.weather.gov'
BASE_NOMINATIM_URL = 'https://nominatim.openstreetmap.org'

def get_lat_lon(string: str) -> float:
    '''
    This function converts the user input and returns floats representing the latitude and longitude given 
    '''
    filtered = string.split(",")
    if "S" in filtered[0]:
        lat = -float(filtered[0][:-1])
    elif "N" in filtered[0]:
        lat = float(filtered[0][:-1])
    if "W" in filtered[1]:
        lon = -float(filtered[1][:-1])
    elif "E" in filtered[1]:
        lon = float(filtered[1][:-1])

    return lat, lon

def build_search_url(latitude: int, longitude: int) -> str:
    '''
    This function takes a latitude and longitude, and builds and returns a URL that can be used to ask
    NWS API for information about the location
    '''

    return f'https://api.weather.gov/points/{str(latitude)},{str(longitude)}'



def get_weather_data_url(url: str) -> dict:
    '''
    This function takes a URL and gets a Python dictionary representing
    the parsed JSON response and gets the required url and returns it.
    '''
    response = None

    try:
        # Here, we open the URL and read the response, just as we did before.
        # After the third line, json_text will contain the text of the
        # response, which should be in JSON format.
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        json_text = response.read().decode(encoding = 'utf-8')
        

        # Given the JSON text, we can use the json.loads() function to convert
        # it to a Python object instead.
        result = json.loads(json_text)
        return str(result['properties']['forecastHourly'])
    
    finally:
        # We'd better not forget to close the response when we're done,
        # assuming that we successfully opened it.
        if response != None:
            response.close()


def get_data(url: str) -> dict:
    '''
    This function takes a url and returns a Python dictionary containing data about the specified location
    '''
        
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        json_text = response.read().decode(encoding = 'utf-8')

        return json_text
        # return json.loads(json_text)

    finally:
        # We'd better not forget to close the response when we're done,
        # assuming that we successfully opened it.
        if response != None:
            response.close()

def get_file_data(path: Path):
    f = open(Path(path), 'r')
    data = json.load(f)
    return data

def forward_geocode_url(name: str) -> str:
    
    query_parameters = [
        ('q', name), ('format', 'json')
    ]
    return f'{BASE_NOMINATIM_URL}/search?{urllib.parse.urlencode(query_parameters)}'

def reverse_geocode_url(lat: int, lon: int) -> str:
    query_parameters = [
        ('lat', str(lat)), ('lon', str(lon)), ('format', 'json')
    ]
    return f'{BASE_NOMINATIM_URL}/reverse?{urllib.parse.urlencode(query_parameters)}'

# def first_line():
#     array = first_line.split(" ")
#     name = ' '.join(array[2:])
#     if ' '.join(array[0:2]) == "TARGET NOMINATIM":
#         url = forward_geocode_url(name)
#         data = get_data(url)
#         with open('location_file.json', 'w') as f:
#             f.write(str(data))
#         data = get_file_data('location_file.json')
#         lat, lon = data[0]['lat'], data[0]['lon']
    
def run_first_line(line: str) -> float:
    array = line.split(" ")
    command = " ".join(array[0:2])
    name_or_path = " ".join(array[2:])
    if command == "TARGET NOMINATIM":
        url = forward_geocode_url(name_or_path)
        data = get_data(url)
        with open('location_file.json', 'w') as f:
            f.write(data)
        data = get_file_data('location_file.json')
        lat, lon = data[0]['lat'], data[0]['lon']
    elif command == "TARGET FILE":
        data = get_file_data(name_or_path)
        print(command, name_or_path)
        lat, lon = data[0]['lat'], data[0]['lon']
    return lat, lon

def run_second_line(line: str, lat: float, lon: float):
    array = line.split(" ")
    command = " ".join(array[0:2])
    if line == "WEATHER NWS":
        url = build_search_url(lat, lon)
        weather_url = get_weather_data_url(url)
        data = get_data(weather_url)
        with open('weather_file.json', 'w') as f:
            f.write(data)
        path = Path('weather_file.json')
    elif command == 'WEATHER FILE':
        path = " ".join(array[2:])
        data = get_file_data(path)

    if float(lat) < 0:
        lat = str(-float(lat)) + "/S"
    else:
        lat = str(lat) + "/N"

    if float(lon) < 0:
        lon = str(-float(lon)) + "/W"
    else:
        lon = str(lon) + "/E"
    print('TARGET ' + str(lat) + " " + str(lon))
    return data, path

def get_station_location(path: Path):
    f = open(path, 'r')
    data = json.load(f)
    lats = []
    lons = []
    for coords in data['geometry']['coordinates'][0]:
        lat = coords[1]
        lon = coords[0]
        if lat not in lats:
            lats.append(lat)
        if lon not in lons:
            lons.append(lon)
    average_lat = sum(lats)/len(lats)
    average_lon = sum(lons)/len(lons)

    # if average_lat < 0:
    #     average_lat = str(-average_lat) + "/S"
    # else:
    #     average_lat = str(average_lat) + "/N"

    # if average_lon < 0:
    #     average_lon = str(-average_lon) + "/W"
    # else:
    #     average_lon = str(average_lon) + "/E"

    return average_lat, average_lon

def run_fifth_line(path):
    with open(path, 'r') as f:
        data = json.load(f)
    print(data['display_name'])


def run() -> None:
    weather_queries = []
    first_line = input().strip()
    second_line = input().strip()
    # weather_query = input().strip()
    # weather_queries.append(weather_query)
    # while True:
    #     weather_query = input().strip()
    #     if weather_query == "NO MORE QUERIES":
    #        break 
    #     weather_queries.append(weather_query)
    fifth_line = input().strip()

    lat, lon = run_first_line(first_line)
    data, path = run_second_line(second_line, lat, lon)

    if fifth_line == "REVERSE NOMINATIM":
        lat, lon = get_station_location(path)
        url = reverse_geocode_url(lat, lon)
        with open('reverse_nominatim.json', 'w') as f:
            data = get_data(url)
            f.write(data)
        run_fifth_line('reverse_nominatim.json')
    else:
        array = fifth_line.split(' ')
        path = ' '.join(array[2:])
        run_fifth_line(path)




    


    # lat, lon = get_lat_lon(coords)
    # geocode_url = reverse_geocode_url(lat, lon)
    # data = get_data(geocode_url)
    # print(data)

if __name__ == '__main__':
    run()