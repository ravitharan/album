import sys
from GPSPhoto import gpsphoto
from geopy.geocoders import Nominatim

def get_location(image):
    """
        Get the data from image file and return a dictionary
        location : Kadaiparichchan, තිරිකුණාමළය දිස්ත්‍රික්කය, கிழக்கு மாகாணம், ශ්‍රී ලංකාව இலங்கை

    """
    data = gpsphoto.getGPSData(image) # {'Longitude': 81.29380833333333, 'Latitude': 8.45251111111111}
    Latitude = data['Latitude']
    Longitude = data['Longitude']

    geolocator = Nominatim(user_agent="geoapiExercises") # Initialize Nominatim API
    location = geolocator.geocode(str(Latitude) + "," + str(Longitude)) # Get location with geocode
    
    return location

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Argument error\nUsage: {sys.argv[0]} <jpeg_file>\n')
        exit(1)
    image = sys.argv[1]
    location = get_location(image)

    print("\nLocation of the given Latitude and Longitude: ",location) # Display location


