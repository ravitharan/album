import sys
from PIL import Image, ExifTags
from datetime import datetime
import googlemaps

META_TAGS = [ 'ImageWidth', 'ImageLength', 'DateTime', 'GPSInfo' ]

def convert_exif_gps(GPSInfo):
    """
        GPSInfo : {  0: b'\x02\x02\x00\x00',
                     1: 'N',
                     2: (51.0, 37.0, 26.937561),
                     3: 'W',
                     4: (0.0, 47.0, 15.003519),
                     5: b'\x00',
                     6: 197.6,
                     7: (9.0, 41.0, 42.0),
                    27: 'CELLID',
                    29: '2021:12:19'}

    """
    latitude = GPSInfo[2][0] + GPSInfo[2][1]/60.0 + GPSInfo[2][2]/60.0/60.0
    if GPSInfo[1] == 'S':
        latitude *= -1

    longitude = GPSInfo[4][0] + GPSInfo[4][1]/60.0 + GPSInfo[4][2]/60.0/60.0
    if GPSInfo[3] == 'W':
        longitude *= -1

    gmaps = googlemaps.Client(key='AIzaSyDCiQZ-znivMvi-6-lvjAMK1wWl2pBQIfA')

    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))

    return reverse_geocode_result[0]['formatted_address']

def get_picture_metadata(image, meta_tags):
    """
    metadata 
        {'ImageWidth': 2560, 'ImageLength': 1440,DateTime': '2020:11:17 15:58:52',...}

    """
    metadata = {}
    
    image = Image.open(image)
    exifdata = image.getexif()
    if exifdata is None:
        print('Sorry, image has no exif data.') 
    else:
        for key, value in exifdata.items():
            if key in ExifTags.TAGS:
                tag_name = ExifTags.TAGS[key]
                if tag_name in meta_tags:
                    if tag_name == 'DateTime':
                        value = datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
                    elif tag_name == 'GPSInfo':
                        value = convert_exif_gps(value)
                    metadata[tag_name] = value
    return metadata

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Argument error\nUsage: {sys.argv[0]} <jpeg_file>\n')
        exit(1)
    image = sys.argv[1]

    metadata = get_picture_metadata(image, META_TAGS)
    for tag in META_TAGS:
        print(f'{tag:12}: {metadata[tag]}')
