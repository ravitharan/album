from PIL import Image
from PIL.ExifTags import TAGS
import os
FILENAMES = []
roots = []
for root, dirs, files in os.walk(r"C:\Users\A2Z Lankan\Desktop\sithu"):
    roots.append(root)
    for filename in files:
        if filename.endswith(".jpg"):
            FILENAMES.append(filename)
for root in roots:
    for file in FILENAMES:
        str_var = root + "\\" + file
        image = Image.open(str_var)
        print(root + "\\" + file)
        exifdata = image.getexif()
        for tag_id in exifdata:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
             # decode bytes 
            if isinstance(data, bytes):
                data = data.decode()
            print(f"{tag:50}: {data}")
        
        print ("Error: can\'t find file or read data")
        


class photo_org():
    def __init__(self, photo_path):
        self.path = photo_path

    def meta_data(self):
        image = Image.open(self.path)
        exifdata = image.getexif()
        for tag_id in exifdata:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            # decode bytes 
            if isinstance(data, bytes):
                data = data.decode()

            print(f"{tag:50}: {data}")
        
