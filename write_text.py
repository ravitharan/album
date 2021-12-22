from PIL import Image, ImageFont, ImageDraw
from PIL.ExifTags import TAGS
import sys

def write_text(img):
    img = Image.open(img)
    width, height = img.size
    font = ImageFont.truetype("arial.ttf", 50)
    draw = ImageDraw.Draw(img)
    exifdata = img.getexif()
    text = ""
    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        if isinstance(data, bytes):
            data = data.decode()
        if tag == "DateTime":
            text = data
    if width > height:
        new_width = (width-(width-30))
        new_height = (height-70)
        print(new_width,new_height)
        draw.text((new_width,new_height),text,(0, 0, 0),font=font)
    else:
        new_width = (width-(width-20))
        new_height = (height-50)
        font = ImageFont.truetype("FONTS/arial.ttf", 30)
        draw.text((new_width,new_height),text,(0, 0, 0),font=font)
    img.save("text.png")
if _name_ == '_main_':
    if len(sys.argv) != 2:
        print(f'Argument error\nUsage: {sys.argv[0]} <jpeg_file>\n')
        exit(1)
    image = sys.argv[1]

    write_text(image)
    
