import sys
import exifread
from geopy.geocoders import Nominatim

def get_location(image):
    """
        location : Kadaiparichchan, තිරිකුණාමළය දිස්ත්‍රික්කය, கிழக்கு மாகாணம், ශ්‍රී ලංකාව இலங்கை

    """
    def get_latitude_longitude(data):
        """
            class : 'str'
            data : [8, 27, 297/20]
                   [81, 17, 1059/50]
        
        """
        list_tmp = str(data).replace('[', '').replace(']', '').split(',') # ['8', ' 27', ' 297/20']
        list=[ele.strip() for ele in list_tmp] # ['8', '27', '297/20']
        data_sec = int(list[-1].split('/')[0]) /(int(list[1].split('/')[-1])*3600)# Second value, data_sec: 0.0030555555555555557,class 'float' 
        data_minute = int(list[1])/60 # data_minute : 0.0030555555555555557, class 'float'
        data_degree = int(list[0]) # 8 class 'int' 
        result = data_degree + data_minute + data_sec # 8.453055555555554
         
        return result
    
    img=exifread.process_file(open(image,'rb'))
    Latitude=str(get_latitude_longitude(str(img['GPS GPSLatitude']))) # 8.453055555555554
    Longitude=str(get_latitude_longitude(str(img['GPS GPSLongitude']))) # 81.30063725490196
    geolocator = Nominatim(user_agent="geoapiExercises") # Initialize Nominatim API
    location = geolocator.geocode(Latitude+","+Longitude) # Get location with geocode

    return location

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Argument error\nUsage: {sys.argv[0]} <jpeg_file>\n')
        exit(1)
    image = sys.argv[1]
    location = get_location(image)
     
    #print("Latitude: ", Latitude,"\nLongitude: ", Longitude) # Displaying Latitude and Longitude

    print("\nLocation of the given Latitude and Longitude: ",location) # Display location


