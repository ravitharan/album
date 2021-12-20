import sys
from PIL import Image, ExifTags

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
