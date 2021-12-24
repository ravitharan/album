import sys
from PIL import Image, ExifTags
from datetime import datetime
import re

'''
TODO:
1) Convert date string into datetime object
2) Convert GPSInfo into cordinate
'''

def get_picture_metadata(image):
    """
    metadata 
        {'ImageWidth': 2560, 'ImageLength': 1440,DateTime': '2020:11:17 15:58:52',...}

    """
    meta_tags = [ 'ImageWidth', 'ImageLength', 'DateTime', 'GPSInfo' ]
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
                        value_list = re.split(' +',value) # value : 2020:09:26 10:01:46, value_list : ['2020:09:26', '10:01:46'] 
                        datetime_value = ((value_list[0].replace(':','-'))+ " " + value_list[1]) # datetime_value : 2020-09-26 10:01:46 (class 'str'>
                        value = datetime.fromisoformat(datetime_value) # value : 2020-09-26 10:01:46 (class 'datetime.datetime') 
                        metadata[tag_name] = value
                        
                    else:
                        metadata[tag_name] = value
    return metadata

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Argument error\nUsage: {sys.argv[0]} <jpeg_file>\n')
        exit(1)
    image = sys.argv[1]

    metadata = get_picture_metadata(image)
    for tag in metadata:
        print(f'{tag:25}: {metadata[tag]}')
