from PIL import Image
from PIL.ExifTags import TAGS

def meta(photo_name):
    photo = Image.open(photo_name)
    exifdata = photo.getexif()
    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # decode bytes 
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:25}: {data}")
    
    
