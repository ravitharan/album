import sys
import exifread
from datetime import datetime
import googlemaps

WIDTH_KEY       = 'width'
HEIGHT_KEY      = 'height'
ORIENTATION_KEY = 'orientation'
DATE_KEY        = 'date'
LOCATION_KEY    = 'location'

WIDTH_LABEL         = 'Image ImageWidth'
HEIGHT_LABEL        = 'Image ImageLength'
ORIENTATION_LABEL   = 'Image Orientation'
DATE_LABEL          = 'Image DateTime'
GPS_NS_LABEL        = 'GPS GPSLatitudeRef'
GPS_LATITUDE_LABEL  = 'GPS GPSLatitude'
GPS_EW_LABEL        = 'GPS GPSLongitudeRef'
GPS_LONGITUDE_LABEL = 'GPS GPSLongitude'


def get_exif_tags(image):
    """
    metadata 
        {'width': 2560, 'height': 1440, 'orientation': '2020:11:17 15:58:52',...}

    """
    metadata = {}
    latitude = 1
    longitude = 1
    address = ''

    with open(image, 'rb') as img_in:
        tags = exifread.process_file(img_in)
        for key, value in tags.items():
            if not isinstance(value, bytes):
                print(f'{key:25}: {value}')
            if (key == WIDTH_LABEL):
                metadata[WIDTH_KEY] = value.values[0]
            elif (key == HEIGHT_LABEL):
                metadata[HEIGHT_KEY] = value.values[0]
            elif (key == ORIENTATION_LABEL):
                metadata[ORIENTATION_KEY] = value.values[0]
            elif (key == DATE_LABEL):
                value = datetime.strptime(str(value), "%Y:%m:%d %H:%M:%S")
                metadata[DATE_KEY] = value.strftime("%Y %m %d %H %M %S")
            elif (key == GPS_NS_LABEL):
                if value.values[0] == 'S':
                    latitude *= -1
            elif (key == GPS_LATITUDE_LABEL):
                value = value.values
                latitude *= value[0] + value[1]/60.0 + value[2]/3600.0
            elif (key == GPS_EW_LABEL):
                if value.values[0] == 'W':
                    longitude *= -1
            elif (key == GPS_LONGITUDE_LABEL):
                value = value.values
                longitude *= value[0] + value[1]/60.0 + value[2]/3600.0

    if latitude != 1 and longitude !=1:
        gmaps = googlemaps.Client(key='Enter api key here')

        # Look up an address with reverse geocoding
        reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))

        address = reverse_geocode_result[0]['formatted_address']
        print(f'{"location":25}: {address}')

    metadata[LOCATION_KEY] = address

    return metadata

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Argument error\nUsage: {sys.argv[0]} <jpeg_file>\n')
        exit(1)
    image = sys.argv[1]

    metadata = get_exif_tags(image)
    for tag in metadata:
        print(f'{tag:12}: {metadata[tag]}')
