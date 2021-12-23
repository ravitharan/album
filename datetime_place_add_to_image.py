from get_metadata import *
from get_shooting_place import *
import sys
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def date_time_location_add_to_image(image, metadata,location):
    """
        The date time and place will be added in the lower left corner of the image
            '2020-09-26 10:01:46 , Kadaiparichchan'
        
    """
    image_name = (os.path.split(image)[-1])
    image = Image.open(image_name)
    width, height = image.size
    
    draw = ImageDraw.Draw(image)
    Date_Time = str(metadata['DateTime']) # 2020-09-26 10:01:46
    location = str(location) # Kadaiparichchan, තිරිකුණාමළය දිස්ත්‍රික්කය, கிழக்கு மாகாணம், ශ්‍රී ලංකාව இலங்கை
    if width > height:
        new_width = (width-(width-40))
        new_height = (height-80)
        font = ImageFont.truetype("FONTS/arial.ttf",50)
        draw.text((new_width,new_height),Date_Time + ', '+ location,(0,0,0),font=font)
    else:
        new_width = (width-(width-20))
        new_height = (height-50)
        font = ImageFont.truetype("FONTS/arial.ttf",25)
        draw.text((new_width,new_height),Date_Time + ', '+ location,(0,0,0),font=font)    
        
    data_add_image = image.save("COPY--"+image_name)

    return data_add_image

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Argument error\nUsage: {sys.argv[0]} <jpeg_file>\n')
        exit(1)
    image = sys.argv[1]
    metadata = get_picture_metadata(image)
    location = get_location(image)
    data_add_image = date_time_location_add_to_image(image, metadata,location)
    

